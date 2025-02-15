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

## 实物图
一共印制了 6 个板子。即便还是邮票孔的蓝牙模块，也挺贵的。等我有钱了，一定买够。先买 3 个蓝牙模块，完全可以验证一主多从的配置，就这样。</br>
第一个手工焊接的板子，原理图上的所有元件都已焊接。原理图上，部分功能设计的有冗余，考虑到不一定非得买到所有的元件，可以用一定的方式替代。既然它是最全的，把它配置为`Master` role。
另外2个，很明显的是，部分预留的元件未焊接，焊接的共阳极`LED`不是很亮，但是不影响功能。其中又有一个蓝牙模块焊接的有些跑偏，也能用。
1. 印制的PCB板
![PCB空板](https://github.com/Iflier/BTCluster/blob/master/images/PCB%E7%A9%BA%E6%9D%BF.jpg)
2. 已经焊接好的蓝牙模块
![已经焊接好的模块](https://github.com/Iflier/BTCluster/blob/master/images/%E5%85%A8%E9%83%A8%E7%9A%84%E6%9D%BF%E5%AD%90.jpg)
![](https://github.com/Iflier/BTCluster/blob/master/images/%E7%84%8A%E6%8E%A5%E5%A5%BD%E7%9A%84.jpg)
![](https://github.com/Iflier/BTCluster/blob/master/images/%E7%84%8A%E6%8E%A5%E5%A5%BD%E7%9A%842.jpg)
![](https://github.com/Iflier/BTCluster/blob/master/images/%E7%84%8A%E6%8E%A5%E5%A5%BD%E7%9A%843.jpg)
3. 配置好的一主多从连接（当模块有连接时，`LINK`引脚输出低电平，反映到本模块上，表现为共阳极的`LED`会点亮一个）
![一主多从配置](https://github.com/Iflier/BTCluster/blob/master/images/%E8%BF%9E%E6%8E%A5%E6%88%90%E5%8A%9F.jpg)
4. 用于控制`PWM`波的频率和占空比
![一种应用](https://github.com/Iflier/BTCluster/blob/master/images/%E5%BA%94%E7%94%A8.jpg)
![](https://github.com/Iflier/BTCluster/blob/master/images/%E5%BA%94%E7%94%A82.jpg)


## 应用场景
本套系统设计之目的是为了取代正在使用的[蓝牙方法](https://github.com/Iflier/fanAndBLT)。现在使用的蓝牙只能是一主一从方式下的`一对一`连接，如果我想控制更多的风扇，还得重建一套同样的系统。而且没有集中控制的途径，有种大权在握的感觉，真好?!</br>
这一套系统很不一样，在事先绑定了即将加入的模块的`MAC`之后，只要`Master`开机，新的节点可以随时加入和退出，完全没有影响。想要控制更多的散热设备和风扇功率，加入一个蓝牙模块就是了。</br>
当然其应用场景不止于此，除了可以接收数据，还可以主动给`Master`节点发送数据，其他传感器可以发送数据给`Master`。
代价也是有的，就是成本更贵了。</br>
1. 管理多个设备的散热</br>
如本方案之目的。现在我可以把`Master`节点连接到我使用计算机，然后加入其他的节点，它们可以是为不同的设备提供散热的节点。我想调整各个设备的散热风扇功率大小，只在连接`Master`节点的计算机上发送数据即可</br>
2. 不能联网的传感器数据采集</br>
比如室内空气质量监测
3. 家用场景下的智能控制</br>
这需要附加其他控制器


## 目前存在的问题
1. 按键未标注功能</br>
PCB板子上存在两个4脚按键。尽管给不同功能的按键使用了不同的形状，但是如果能在`F.Silks`层标注一下，会更好
2. 同时上电，导致计算机的USB端口停止供电</br>
电源输入端并入容量太大的电容器，当`3`个及以上的模块同时上电时，导致计算机的USB端口停止供电。这是因为电容容量大，在上电的瞬间电容器充电，其充电电流超过了USB端口允许的电流导致USB端口主动停止供电。同时给`2`个模块上电是没问题的。
这是由于现有材料的局限性导致的。由于手头上有这样的电容，再买的话，不得花钱不是？
3. 3.3V的输出并入大容量的电容器</br>
导致的问题是，在关断输入端的电源后，3.3V输出端的电容存储的电量不能合理的释放。（至于电容容纳的电荷究竟都到哪去了？不是还有`ESR`吗？）
4. 输入电压受限</br>
这套系统的核心是蓝牙模块，它使用的是`3.3V`的直流电，其他辅助电路则可以变化。要是有`高效率`（整个系统的功耗也不大，如果降压电路消耗的功率不被约束的话，岂不是不划算？）的直流降压电路，使用起来会更方便。这样，输入电压就不受约束了（目前只能使用直流5V的输入电压）

## 解决方案
1. 针对问题1，已经在新的PCB图上修改了</br>
2. 可以给并入到电源输入端的电容器串入一个较小阻值的电阻</br>
3. 简单点可以串入一个电阻，用它来消耗电容器存储的能量。或者在`3.3V`输出端点亮一个`LED`都行。自己玩，不怎么考虑成本，有什么用什么。</br>

# License
GPL V3.0
