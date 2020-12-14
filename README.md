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
