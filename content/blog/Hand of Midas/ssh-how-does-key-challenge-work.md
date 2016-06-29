title:SSH学习笔记之--Key Challenge 如何工作 
Date: 2015-08-27 10:20
Modified: 2015-08-27 10:20
Tags: SSH, Key Challenge 
Slug: how-does-key-challenges-work
####Key Challenge 如何工作
	
agent非常聪明的一点就是他可以不用将private key暴露给任何人就可以确认一个人的身份（确切的说是拥有私钥的人）。  
	
当用户ssh登陆一台远端服务器的时候，发送包含username和key的请求，其中的username帮助服务器确定其公钥的位置--一般在`$HOME/.ssh/authorized_keys`  
	
服务器端生成一个challenge，其唯一可以被拥有私钥的设备答复。服务器产生并保存一个大的随机数，然后以用户的公钥进行加密，将生成的二进制数据发送给请求的用户。对于没有私钥的用户这些数据没有任何意义。  
	
当agent接受到challenge, 它用私钥进行解密，获得远端服务器生成的原始随机数。agetn把获得的随机数，附加SSH session ID(该值每一个连接都不一样)，进行md5加密，作为key response返回给服务器。  
	
服务器计算相同的md5（根据随机数和SSH session ID），与返回的key response进行对比，如果匹配则认证成功。如果不对的话，agent里面的下一个私钥将被用来进行相同的尝试，直到成功或者因为所有的私钥尝试完而失败。  
	
很明显，原始的随机数在client/agent交互的时候并不会被暴露，这也是基于安全性考虑以防止在client/server信息交互的过程中随机数被获取。

![alt](http://www.unixwiz.net/images/ssh-key-challenge.gif "Title")
![alt](http://www.unixwiz.net/images/ssh-key-response.gif)
