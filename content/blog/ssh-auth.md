title:SSH学习笔记之--SSH 认证 
Date: 2015-08-27 10:20
Modified: 2015-08-27 10:20
Category: SSH 
Tags: SSH, Auth 
Slug: ssh-auth 
Authors: nullne 
###SSH认证过程
首先感谢Steve Friedlde 的文章[An Illustrated Guide to SSH Agent Forwarding](http://www.unixwiz.net/techtips/ssh-agent-forwarding.html)，感谢[SSH Agent Forwarding原理](http://blog.csdn.net/sdcxyz/article/details/41487897)(注：该文也为转载，但是原博链接已经失效)。本文主要内容参考引用自这两篇文章，并做了部分错误勘正。
####密码认证  
密码认证最简单，下面是认证步骤:  
    
    1. ssh client向目标机器发起tcp连接(一般22端口)并发送username (username是SSH协议的一部分)
    2. 目标机器ssh daemon回应需要密码
    3. ssh client提示用户输入密码，然后将密码发送到服务器端
    4. ssh daemon如果密码匹配成功, 则认证通过 
     
基于密码认证的缺点是：

    1. 容易被brute-force password guessing
    2. 不适合于管理多台机器
    3. 若每台机器使用相同的密码，如果密码泄露，所有机器都被攻破。若使用不同密码，则密码太多很难记住，因此也不可能使用很强的密码。
    
####公钥认证  
公钥认证详细协议见RFC4252的publickey部分  
 	
公钥认证需要先在本地机器生成公钥私钥对，然后将公钥放到目标机器的$HOME/.ssh/authorized_keys中。具体过程如下
 		
 	1. ssh client向目标机器发起tcp连接(一般22端口)，并发送包含username和key的请求
 	2. 目标机器在本地authoriaed_keys 中查找对应信息，创建基于所查找到的公钥的challenge,发送到ssh client
 	3. ssh client接收到challenge之后，在本机查找对应的私钥，如果私钥被passphrase加密的话提示用户输入passphrase以解密私钥
 	4. ssh client发送私钥签名的challenge给等待的ssh daemon
 	5. 目标机器验证返回信息，如果有效则通过认证
 	
 如果公钥认证失败，ssh还会尝试其他认证策略，比如密码认证。多个认证策略的尝试顺序和服务器端没关系，由客户端的配置来决定。  
 	
 需要说明的是，即使把本机的公钥(如.ssh/id_rsa.pub)删除掉，认证仍然可以成功。那第三步中提到的公钥从哪里来的呢？实际上，上面(如第二步)提到的私钥(如.ssh/id_rsa)是广义的，既包含了私钥，也包含了公钥，也有可能还包含了其他信息(比如证书)。比如通过ssh-keygen -y ~/.ssh/id_rsa就可以看到id_rsa里面的公钥。  
 	
 用作认证的私钥最好通过passphrase进行加密，否则会有很大安全隐患，只要私钥泄露，别人就能访问你能访问的所有远程机器。
	
公钥认证由于需要配置公钥私钥，初始配置稍微麻烦一些，但好处是所有机器只需配置一组公私钥对就可以了。由于只有一个私钥，不必设置多个密码，因此可以为其设置比较强的密码。并且仅当私钥和密码一同丢失时才有风险，但这个概率非常小。

不过仍然烦人的是，每次登陆都得输入passphrase。
####使用ssh-agent的公钥认证    
为解决每次登陆远程机器都需要输入passphrase的问题，ssh-agent被引入了。ssh-agent启动后，可通过ssh-add将私钥加入agent. ssh-add会提示用户输入passphrase以解密私钥，然后将解密后的私钥纳入agent管理。agent可同时管理多个私钥。  
    
连接服务器的步骤如下:

    1. ssh client向目标机器发起tcp连接(一般22端口)，并发送包含username和key的请求
    2. 目标机器在本地authorized_keys 中查找对应信息，创建基于所查找到的公钥的challenge,发送到ssh client
    3. ssh client 接收到challenge并把它扔给运行中的agent，agent,而不是ssh client本身打开用户私钥，如果被加密需要输入passphrase
    4. agent将私钥签名的信息返回给client, 然后再发送到目标机器的ssh daemon
    5. 目标机器校验返回信息，如果有效则通过认证

如果ssh-agent中有多个私钥, 会依次尝试，直到认证通过或遍历所有私钥.  

在整个过程中，私钥只存在于agent的内部(内存中), ssh client并没有获取到私钥。  

使用ssh-agent后，只需在将key纳入agent管理时输入passphrase，之后的ssh相关操作就不必输入passphrase了。但如果从本机A登陆机器B后，又想从B登陆C (或从B传输文件到C)，仍然需要输入passphrase (如果B上也配置了用户的私钥)或password。还是比较麻烦。  

幸好，ssh agent forwarding解决了这一问题。  

####使用ssh-agent forwarding的公钥认证  
	
简而言之，ssh-agent forwarding 允许一系列的ssh连接将key challenges依次返回给最初的ssh-agent，避免了在其他中间机器上面输入密码的麻烦。  
	
步骤如下：
	1. 假设用户已经从本地机器连接到了第一台机器server。本地的agent中已保存了用户的私钥
	2. 用户从server向server2请求ssh连接， 发送包含username和key的请求
	3. server2的ssh daemon查询authorized_keys文件，根据查找到的key构建challenge并发回server
	4. 神奇的事情发生了：server机器上的client接受了这个challenge，把它发送到本台机器的sshd,sshd又将challenge发送到之前与本地机器建立的连接中，本地机器的client最终处理这个challenge,将签名之后的信息延相反的方向传递
	5. server2上的daemon校验返回信息，如果有效则通过认证建立连接  
	
注意server上其实ssh-agent压根就没有启动，ssh client只是检查$SSH_AUTH_SOCK这个环境变量是否存在，如果存在，则和这个变量指定的domain socket进行通信。而这个domain socket其实是由server上的sshd创建的。所以ssh client其实是和sshd在通信。  
	
而server的sshd并没有私钥信息，所以sshd做的事情其实是转发该请求到homepc的ssh client，再由该client将请求转发给本地(homepc)的agent。该agent将需要的消息和签名准备完毕后，再将此数据按原路返回到server的ssh client. 路径如下所示:
	  
	agent_local --》($SSH_AUTH_SOCK)--》 ssh_local --》(tcp)--》  sshd_server --》($SSH_AUTH_SOCK)--》 ssh_server --》(tcp)--》  sshd_server2
		  
这下明白为什么叫agent forwarding(转发)了吧，就是所有中间节点的sshd和ssh都充当了数据转发的角色，一直将私钥操作的request转发到了本机的agent，然后再将agent的response原路返回。  

####SSH proxy  
