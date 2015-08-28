title:SSH学习笔记之--SSH 配置技巧  
Date: 2015-08-27 10:20  
Modified: 2015-08-27 10:20  
Category: SSH   
Tags: SSH, config  
Slug: ssh-config-tips  
Authors: nullne  
###SSH配置技巧
#####配置主机别名, 省略用户名
修改（创建如果不存在）~/.ssh/config,  增加下面条目(可添加多个)

```
Host cc
HostName 192.168.1.1
Port 22
User root
```

之后就可以直接这样登录，如果配置了密钥登录的话就连密码也不需要输入了

```
ssh cc
```
#####配置密钥登录
1. 生成私钥公钥对

	```
	$ ssh-keygen -t rsa                                                    #生成RSA类型的密钥对  
	Generating public/private rsa key pair.  
	Enter file in which to save the key (/home/yule/.ssh/id_rsa):          #输入密钥存放位置，直接回车为默认值  
	Enter passphrase (empty for no passphrase):                            #输入密钥密码，用来解锁密钥  
	Enter same passphrase again:  
	Your identification has been saved in /home/yule/.ssh/id_rsa.  
	Your public key has been saved in /home/yule/.ssh/id_rsa.pub.  
	The key fingerprint is:  
	3c:13:20:5c:80:02:3d:e5:64:44:3e:69:2b:83:b9:d8 yule@client.cc.test  
	The key's randomart image is:  
	+--[ RSA 2048]----+  
	|o. *Ooo          |  
	|. +=.o .         |  
	| . .*   .        |  
	| o . o . .       |  
	|o o .   S        |  
	|.o o     o       |  
	|o E              |  
	|                 |  
	|                 |  
	+-----------------+  
	```  

2. 将公钥拷贝到需要ssh登录的服务器

	如果当前机器有`ssh-copy-id`命令的话将会非常方便:  
	`ssh-copy-id [-i [identity_file]] [user@]machine`  
	
	否则需要手动拷贝到目标机器上面，然后把内容添加到目标机器的*$HOME/.ssh/authorized_keys*文件内：  
	
	```
	scp ~/.ssh/id_rsa.pub [usr@]machine:/tmp
	ssh [usr@]machine
	cat /tmp/id_rsa.pub >> ~/.ssh/authorized_keys
	```

3. 修改相关文件权限
	
	ssh对于文件权限非常敏感，通常无法通过ssh密钥登录很有可能就是因为文件权限出错。注意下面的权限为目标机器的权限。
	1. ~/.ssh 目录权限为700: `chmod 700 ~/.ssh`
	2. ~/.ssh/authorized_keys 文件权限为600: `chomod 600 ~/.ssh/authorized_keys`

这样不出意外的话，此时就可以使用密钥（无需输入密码）登录远端服务器了。
####使用Agent管理密钥
关于Agent的介绍，请参照系列文章[]()

```
eval `ssh-agent -s`             #启动ssh-agent
ssh-add	[-i file]               #添加默认位置的密钥，如果密钥被密码加密的话需要输入密码,可指定私钥位置
ssh-add -D|-d                   #删除（全部）密钥
```

####配置Agent Forwarding
可以在你的ssh配置中改变下面条目，通常在/etc/ssh_config:

```
AllowAgentForwarding yes
```

也可以使用命令，推荐使用后者

```
ssh -A [user@]machine 
```
####建立长连接
可以在你的ssh配置中改变下面条目，通常在/etc/ssh_config.4h 代表连接保持4小时:
```
ControlPersist 4h
```
