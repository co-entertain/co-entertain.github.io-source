title:SSH学习笔记  
Date: 2015-08-27 10:20  
Modified: 2015-08-27 10:20  
Category: SSH   
Tags: SSH  
Slug: learning-ssh  
Authors: nullne  
####SSH 学习笔记
因为工作的原因最近两个礼拜都在看一些跟SSH有关的东西，查阅了大量的资料，其中包括各种博客。最直观的感受就是看博客可能会获得一些小技巧，解决眼下的问题。等到下一次出问题的时候又得大量查阅各种资料（其实主要就是google一下看是否相同的或者类似的需求已经被实现了）。所以当你需要彻底了解一个事情的时候，RFC才是最终的地方。你去看他的标准，从最根本的地方了解他，这样才能彻底的驾驭。  

下面是整理的一些笔记，为方便起见分为几个模块，本文为所有的目录索引。文中直接引用的地方已经标注，部分内容为自己翻译。

#####SSH RFC
认识一个事情最根本也是最彻底的方式就是从他的定义开始，所以如果你不只是用用SSH，而需要更为深入的理解其原理，私人定制部分功能，那么去读一下RFC吧。  
[这儿](nice)简单的把SSH几个部分罗列了一下，更为全面的解释参照[RFC官方文档](http://www.rfc-base.org/txt/rfc-4251.txt)。  


#####SSH认证[^1]
- **密码认证**  
- **公钥认证**  
- **使用ssh-agent的公钥认证**  
- **使用ssh-agent forwarding的公钥认证[^2]**

#####SSH隧道（SSH tunnel)[^3]
- Local Port Forwarding
- Remote Port Forwarding

#####SSH配置技巧
- 配置主机别名, 省略用户名
- 配置密钥登录
- 使用Agent管理密钥
- 配置Agent Forwarding
- 建立长连接

####SSH使用技巧[^4]
- 通过SSH执行命令
- Agent Forwarding
- Enable X mode
- 运行SSH在后台，不需要输出
- psudo-tty allocation

#####SSH Pyhon/Golang实现
- 批量SSH工具  
	此部分的代码日后整理好了之后将给出github地址

#####SSH 开销
#####其他
- **加密**
- **SSH Agent**
- **key challenge如何工作**  
- **公钥和私钥[^5]**
  
	公钥，顾名思义，公开的密钥，即可以通过公开的途径或者仓库让其他人获得。相反，私钥必须只能由持有者获得。因为公钥和私钥在数学上的相关性，凡是被公钥加密的信息都可以由相应地私钥解密，反之亦然。
- **Agent Hijacking**


#####*参考*

1. [Getting started with SSH security and configuration](http://www.ibm.com/developerworks/aix/library/au-sshsecurity/)
2. [ssh详细登录过程 ](http://blog.chinaunix.net/uid-21854925-id-3082425.html)

[^1]: [An Illustrated Guide to SSH Agent Forwarding](http://www.unixwiz.net/techtips/ssh-agent-forwarding.html)
[^2]: [SSH Agent Forwarding原理](http://blog.csdn.net/sdcxyz/article/details/41487897)  
[^3]: [SSH Tunnel - Local and Remote Port Forwarding Explained With Examples](http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html)  
[^4]:[远程登录SSH安全小技巧](http://www.seye.com.cn/newsDetail.lzs?id=959)
[^5]: [Public Key and Private Keys](https://www.comodo.com/resources/small-business/digital-certificates2.php)
