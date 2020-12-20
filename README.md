# 多场景下可灵活接入的无线传输方案

## 简介
本方案使用新一代的蓝牙模块，其突出特点是可连接多个`Master`和`Slave`角色的节点。最多可连接`8`个节点，在本节点被配置为主从一体的情况下，具体来说就是：4个`Master`和4个`Slave`角色。
在事先绑定要连接的节点的`MAC`并且在`Master`开机的情况下，已经绑定`MAC`（配置为`Master`或者`Slave`角色）的节点可随时加入或者退出与`Master` 角色的连接。
一旦与`Master`角色的节点连接成功，它们将不再接收`AT`命令。同时`LINK`引脚输出低电平，指示本模块已连接。
## 为什么？
为什么会创建出这么一套系统？</br>
事情源自于 2014 年的时候，手头上有一个涡轮风扇，标注功率为`12V@2.96A`，`4-Pin`支持调速。直接引入`12V`的直流电，非常简单的方法就可以让其全速运行。但是如何利用它已有的`PWM`调速功能，我一直很好奇。</br>
时间来到 2018 年，期间这件事一直在我心里，不曾忘记，我倒是想忘记。某次在搜索`4-Pin`风扇的引脚连接示意图的时候，有人提到`pwm`引脚可以使用频率为`22.5 KHz`的`PWM`波控制。</br>
整理一下手里已有的单片机，还行，有能用的。接下就发生了：
### [使用`Python`语言给蓝牙模块发送`AT`命令](https://github.com/Iflier/QueryBLT)
### [使用蓝牙控制PWM风扇(`Python`语言)](https://github.com/Iflier/fanAndBLT)
### [使用蓝牙控制PWM风扇(`Go`语言)](https://github.com/Iflier/fanAndBLTGo)
它们的突出特点是控制端的电源不与直流风扇共用。其目的是为了保护控制端，因为控制端直连的是计算机的USB端口。</br>
在调整期间，由于单片机引脚误碰到12V电源，遇到了单片机立即报废的情况。还好不是很贵。
## 原理图
![原理图](https://github.com/Iflier/BTCluster/blob/master/images/Schematic.PNG)
## 即将打印的PCB
![PCB正面](https://github.com/Iflier/BTCluster/blob/master/images/PCB_front.PNG)
![PCB背面](https://github.com/Iflier/BTCluster/blob/master/images/PCB_back.PNG)
## 3D 视图
![3D模型](https://github.com/Iflier/BTCluster/blob/master/images/3D.PNG)

# License
GPL V3.0
