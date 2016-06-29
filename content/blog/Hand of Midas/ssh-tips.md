title:SSH学习笔记之--SSH 使用技巧  
Date: 2015-08-27 10:20  
Modified: 2015-08-27 10:20  
Tags: SSH, tips  
Slug: ssh-tips  
###SSH使用技巧
####通过SSH执行命令

```
ssh [user@]machine "cmd"                                  # 执行单条命令
ssh [user@]machine "bash -s" < shell_script.sh            # 执行脚本
ssh -t [user@]machine "sudo bash -s" < shell_script.sh    # sudo执行
```
####Agent Forwarding

```
ssh -A hostname
```
>     -A     Enables forwarding of the authentication agent connection.  This can also be specified on a per-host basis in a configuration file.
>            Agent forwarding should be enabled with caution.  Users with the ability to bypass file permissions on the remote host (for the agent's UNIX-domain socket) can access the local agent through the forwarded connection.  An attacker cannot obtain key material from the agent, however they can perform operations on the keys that enable them to authenticate using the identities loaded into the agent.
>     -a     Disables forwarding of the authentication agent connection.

####Enable X mode
```
ssh -Xf hostname
```
>     -X      Enables X11 forwarding.  This can also be specified on a per-host basis in a configuration file.
>
>             X11 forwarding should be enabled with caution.  Users with the ability to bypass file permissions on the remote host (for the user's X authorization database) can access the local X11 display through the forwarded connection.  An attacker may then be >able to perform activities such as keystroke monitoring.
>     -x      Disables X11 forwarding.
>
>     -f      Requests ssh to go to background just before command execution.  This is useful if ssh is going to ask for passwords or passphrases, but the user wants it in the background.  This implies -n.  The recommended way to start X11 programs at a remote site is with something like ssh -f host xterm.
>
>             If the ExitOnForwardFailure configuration option is set to ``yes'', then a client started with -f will wait for all remote port forwards to be successfully established before placing itself in the background.

####运行SSH在后台，不需要输出
```
ssh -nNT hostname
```
>     -N      Do not execute a remote command.  This is useful for just forwarding ports (protocol version 2 only).
>
>     -n      Redirects stdin from /dev/null (actually, prevents reading from stdin).  This must be used when ssh is run in the background.  A common trick is to use this to run X11 programs on a remote machine.  For example, ssh -n shadows.cs.hut.fi emacs & will start an emacs on shadows.cs.hut.fi, and the X11 connection will be automatically forwarded over an encrypted channel.  The ssh program will be put in the background.  (This does not work if ssh needs to ask for a password or passphrase; see also the -f
>	  -T      Disable pseudo-tty allocation.

####psudo-tty allocation
```
#分别执行下面两条命令即可明白有什么不同
ssh -t hostname "sudo whoami"
ssh hostname "sudo whoami"
```
>     -t      Force pseudo-tty allocation.  This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful, e.g. when implementing menu services.  Multiple -t options force tty allocation, even if ssh has no local tty.

