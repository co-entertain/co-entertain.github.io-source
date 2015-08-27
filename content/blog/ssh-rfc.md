###SSH RFC
#### [The Secure Shell (SSH) Protocol Architecture](http://www.rfc-base.org/txt/rfc-4251.txt)
>Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network.  It consists of three major components:
>   
>    - The Transport Layer Protocol [SSH-TRANS] provides server
>      authentication, confidentiality, and integrity.  It may optionally
>      also provide compression.  The transport layer will typically be
>      run over a TCP/IP connection, but might also be used on top of any
>      other reliable data stream.
>
>    - The User Authentication Protocol [SSH-USERAUTH] authenticates the
>      client-side user to the server.  It runs over the transport layer
>      protocol.
>
>    - The Connection Protocol [SSH-CONNECT] multiplexes the encrypted
>      tunnel into several logical channels.  It runs over the user
>      authentication protocol.

   The client sends a service request once a secure transport layer
   connection has been established.  A second service request is sent
   after user authentication is complete.  This allows new protocols to
   be defined and coexist with the protocols listed above.

   The connection protocol provides channels that can be used for a wide
   range of purposes.  Standard methods are provided for setting up
   secure interactive shell sessions and for forwarding ("tunneling")
   arbitrary TCP/IP ports and X11 connections.
   
   
####  [The Secure Shell (SSH) Transport Layer Protocol](https://www.ietf.org/rfc/rfc4253.txt)
#### [The Secure Shell (SSH) Authentication Protocol](https://tools.ietf.org/html/rfc4252)
#### [The Secure Shell (SSH) Connection Protocol](https://tools.ietf.org/html/rfc4254)
>   The SSH Connection Protocol has been designed to run on top of the
   SSH transport layer and user authentication protocols ([SSH-TRANS]
   and [SSH-USERAUTH]).  It provides interactive login sessions, remote
   execution of commands, forwarded TCP/IP connections, and forwarded
   X11 connections.
   
   
- **Channel Mehanism**

   All terminal sessions, forwarded connections, etc., are channels.
   Either side may open a channel.  Multiple channels are multiplexed
   into a single connection.
- **Interactive Session**

   A session is a remote execution of a program.  The program may be a
   shell, an application, a system command, or some built-in subsystem.
   It may or may not have a tty, and may or may not involve X11
   forwarding.  Multiple sessions can be active simultaneously.


