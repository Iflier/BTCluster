# -*- coding:utf-8 -*-
import re
import time
import argparse
import binascii
from threading import Lock

import serial
from serial import EIGHTBITS

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", type=str, default="COM5", help="指定使用的串口号，默认为COM5")
ap.add_argument('-b', "--baudrate", type=int, default=115200, help="指定串口通信波特率")
args =vars(ap.parse_args())

class DeviceInstance(object):
    """用于初始化串口设备
    """
    _instanceLock = Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(DeviceInstance, "_instance"):
            with DeviceInstance._instanceLock:
                if not hasattr(DeviceInstance, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance
    def __init__(self, port, baudrate=115200):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.device = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=EIGHTBITS, write_timeout=3.0)
    
    def getDevice(self):
        return self.device

class Controller(object):
    _instanceLock = Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(Controller, "_instance"):
            with Controller._instanceLock:
                if not hasattr(Controller, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self, device):
        super().__init__()
        self.device = device
    
    def readOutputBuffer(self, device):
        """有时候断开重连或者有新的设备加入，master 会打印一些相关信息出来。本方法是用于读取 master 的输入（从连接的计算机的USB端口看）缓冲（buffer）中的内容
        params:
            device: 一个串口实例
        return:
            None
        """
        if device.in_waiting:
            lines = device.readlines()
            for line in lines:
                part, part2 = self.decodeHex2Str(line)
                if part2:
                    print("{0}\t{1}".format(part, part2))
    
    def decodeHex2Str(self, content):
        """
        解析来自蓝牙master的16进制的字节响应，返回设备编号和字符串类型的响应
        params:
            content: 来自master的16进制的响应
        return:
            元组，包括设备编号和响应字符串
        """
        deviceNum, *resp = content
        if deviceNum < 8:
            respStr = "".join([chr(i) for i in resp])
        elif deviceNum == 83:
            deviceNum = "*"
            respStr = "".join([chr(i) for i in content])
        else:
            respStr = None
        return deviceNum, respStr
    
    def commandWriter(self):
        while True:
            command = input("Command ->: ").upper()
            # 在等待命令的时候，master 可能会有状态变化，产生输出
            self.readOutputBuffer()
            if re.search(r"\d+,\w+", command):
                deviceNum, part2 = command.split(',')
                deviceNum = deviceNum.zfill(2)
                if re.match(r"\d+", part2, re.A):
                    # 如果是调整占空比的命令
                    duty = min(max(int(float(part2)), 0), 100)
                    commandStr = "".join(['D', str(duty).zfill(3)])
                    commandHexStr = "".join([deviceNum, commandStr.encode().hex()])
                    self.device.write(bytes.fromhex(commandHexStr))
                elif re.match(r"F\d+(\.+\d+)*", part2, re.I):
                    # 调整频率
                    commandHexStr = "".join([deviceNum, part2.encode().hex()])
                    self.device.write(bytes.fromhex(commandHexStr))
                elif re.match(r"\S+", part2):
                    # 读取当前配置，主要是 read 命令
                    commandHexStr = "".join([deviceNum, part2.lower().encode().hex()])
                    self.device.write(bytes.fromhex(commandHexStr))
                else:
                    print("[ERROR] Unsupported command: {0}".format(command))
            elif command in ['EXIT', 'QUIT']:
                print("Bye.")
                break
            else:
                print("[ERROR] Unsupported command: {0}".format(command))
            time.sleep(0.35)
            while self.device.in_waiting:
                result = self.device.readline()
                slaveNum, respStr = self.decodeHex2Str(result)
                if respStr:
                    print("Response from slave {0} ->: {1}".format(slaveNum, respStr), end="")
        self.device.close()


if __name__ == "__main__":
    serialDev = DeviceInstance(args["port"], baudrate=args['baudrate']).getDevice()
    if serialDev.is_open:
        controller = Controller(serialDev)
        controller.commandWriter()
    else:
        print("[ERROR] Failed to open port: {0}".format(args['port']))
