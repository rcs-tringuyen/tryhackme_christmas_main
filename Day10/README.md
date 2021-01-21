# [Network] SMB

IP: 10.10.192.238

Advent of Cyber 2:

Recap: Using enum4linux to exploit SMB server

### Using enum4linux, how many users are there on the Samba server (10.10.192.238)?
- `enum4linux -U 10.10.192.238`
- 3 users

### Now how many "shares" are there on the Samba server?
- `enum4linux -S 10.10.192.238`
- 4

### Use smbclient to try to login to the shares on the Samba server (10.10.192.238). What share doesn't require a password?
- `smbclient //10.10.192.238/tbfc-santa`

### What directory does..?
- Just `ls` and it's `jingle-tunes`!!
