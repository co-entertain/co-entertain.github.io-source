title:ARP protocol analysis 
Date: 2014-12-03 10:20
Modified: 2010-12-05 19:30
Category: Web 
Tags: Arp,wireshark 
Slug: ARP-protocol 
Authors: nullne 
Summary: Short version for index and feeds
# ARP 协议分析

@[arp|wireshark]

**地址解析协议**，即**ARP**（Address Resolution Protocol） 是根据IP地址获取物理地址的一个TCP/IP协议。


- **工作过程**
- **协议实战分析**
- **安全威胁分析**
----------
### 工作流程
主机A的IP地址为192.168.1.1，MAC地址为0A-11-22-33-44-01；
主机B的IP地址为192.168.1.2，MAC地址为0A-11-22-33-44-02；
当主机A要与主机B通信时，地址解析协议可以将主机B的IP地址（192.168.1.2）解析成主机B的MAC地址，以下为工作流程：
1. 根据主机A上的路由表内容，IP确定用于访问主机B的转发IP地址是192.168.1.2。然后A主机在自己的本地ARP缓存中检查主机B的匹配MAC地址。
2. 如果主机A在ARP缓存中没有找到映射，它将询问192.168.1.2的硬件地址，从而将ARP请求帧广播到本地网络上的所有主机。源主机A的IP地址和MAC地址都包括在ARP请求中。本地网络上的每台主机都接收到ARP请求并且检查是否与自己的IP地址匹配。如果主机发现请求的IP地址与自己的IP地址不匹配，它将丢弃ARP请求。
3. 主机B确定ARP请求中的IP地址与自己的IP地址匹配，则将主机A的IP地址和MAC地址映射添加到本地ARP缓存中。
4. 主机B将包含其MAC地址的ARP回复消息直接发送回主机A。
5. 当主机A收到从主机B发来的ARP回复消息时，会用主机B的IP和MAC地址映射更新ARP缓存。本机缓存是有生存期的，生存期结束后，将再次重复上面的过程。主机B的MAC地址一旦确定，主机A就能向主机B发送IP通信了

### 协议实战分析

> 
测试环境：windows
测试工具: cmd, wireshark

1. 在`cmd`中获取网关ip：10.3.17.1 ![Alt text](./QQ图片20141028221016.png)
2. 配置`wireshap`截取来自网关，即10.3.17.1的arp包，设置如下![Alt text](./QQ图片20141028222301.png)
获取到arp包后停止，见下图![Alt text](./QQ图片20141028222312.jpg)
3. 随机选择一个arp包（最后一个）进行分析![Alt text](./QQ图片20141028222528.png)
- arp包明确定义了Hardware type,Protocol type,Hardware size,Protocol size,Sender Mac  and IP address,Target Mac and IP address(从上面翻译后的内容可以清晰的看到)。
- ARP缓存会持续一段时间（一般为2分钟），之后又进行新一轮的更新。

###安全威胁分析
（因为模拟ARP攻击可能导致局域网内部出错，故此处只做理论分析）
####ARP欺骗
ARP请求为广播形式发送的，网络上的主机可以自主发送ARP应答消息，并且当其他主机收到应答报文时不会检测该报文的真实性就将其记录在本地的MAC地址转换表，这样攻击者就可以向目标主机发送伪ARP应答报文，从而篡改本地的MAC地址表。 ARP欺骗可以导致目标计算机与网关通信失败，更会导致通信重定向，所有的数据都会通过攻击者的机器。
        最简单的攻击方式就是发送固定格式的ARP报文，类似于下面的格式：![Alt text](./QQ图片20141028224008.png)
已知被攻击者的ip以及mac地址（如果不知道可直接使用广播地址`FF.FF.FF.FF`），将其自己的mac地址以及想截获的目标地址IP封装好发送，即能够刷新被欺骗主机的ARP缓存，从而得到本该发往另一个IP的所有包
####ARP cache poisoning
 

