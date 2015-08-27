###SSH Agent
####SSH Agent简介
ssh-agent是专为既令人愉快又安全的处理RSA和DSA密钥而设计的特殊程序，它包括在OpenSSH分发内。不同于ssh，ssh-agent是个长时间持续运行的守护进程（daemon），设计它的唯一目的就是对解密的专用密钥进行高速缓存。

ssh包含的内建支持允许它同ssh-agent通信，允许ssh不必每次新连接时都提示您要密码才能获取解密的专用密钥。对于ssh-agent，您只要使用ssh-add把专用密钥添加到ssh-agent的高速缓存中。这是个一次性过程；用过ssh-add之后，ssh将从ssh-agent获取您的专用密钥，而不会提示要密码短语来烦您了。
####如何使用
启动ssh-agent：

```
eval `ssh-agent -s`
```

很奇怪，为什么不直接执行`ssh-agent -s`，我们来看一下直接运行的结果:

```
$ ssh-agent
SSH_AUTH_SOCK=/tmp/ssh-xDWYq20983/agent.20983; export SSH_AUTH_SOCK;
SSH_AGENT_PID=20984; export SSH_AGENT_PID;
echo Agent pid 20984;
```

正如您所看到的，事实上ssh-agent的输出是一系列bash命令；如果这些命令被执行，则将设置两个环境变量：SSH_AUTH_SOCK和SSH_AGENT_PID。内含的export命令使这些环境变量对之后运行的任何附加命令都可用。唔，如果shell真对这些行进行计算，这一切才会发生，但是此时它们只是被打印到标准输出（stdout）而已。要使之确定，我们需要使用之前的方式进行调用。

然后就可以将私钥导入

```
ssh-add [-i file]    #不指定文件的话默认从~/.ssh/id_rsa读取
```

####不足之处
首先，```eval`ssh-agent` ```每次执行都会启动一个新的ssh-agent副本；这不仅仅是有一丁点儿浪费，而且还意味着您得使用ssh-add向每个新的ssh-agent副本添加专用密钥。如果您只想打开系统上的一个终端或控制台，这没什么大不了的，但是我们中大多数人打开相当多的终端，每次新打开控制台都需要键入密码短语。从技术角度讲，既然一个ssh-agent进程的确应当足够了，要是我们还需这样做，这毫无道理。

有关ssh-agent的缺省设置的另外一个问题是它同cron作业不兼容。由于cron作业是cron进程启动的，这些作业无法从它们的环境中继承SSH_AUTH_SOCK变量，因而也无从知道ssh-agent进程正在运行以及如何同它联系。事实证明这个问题也是可以修补的。
我们在 /etc/profile.d下面新建一个配置文件ssh-agentsh：

	```
	#!/bin/sh

	if [ -f ~/.agent.env ]; then
	. ~/.agent.env >/dev/null
	if ! kill -0 $SSH_AGENT_PID >/dev/null 2>&1; then
	echo "Stale agent file found. Spawning new agent..."
	eval `ssh-agent |tee ~/.agent.env`
	ssh-add
	fi
	else
	echo "Starting ssh-agent..."
	eval `ssh-agent |tee ~/.agent.env`
	ssh-add
	fi
	```
	
####安全问题
ssh-agent本身不会导致安全性问题，但是因为其将私钥存放在内存中，如果目标机器的admin用户不可信赖，很有可能导致用户密钥信息泄露。
####其他
更多用法参见ssh-agent man pages