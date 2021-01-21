# [Blue Team] Password Manager & CyberChef

IP: 10.10.194.139

Advent of Cyber 2: 

- Today we continue to use Remmina and decrypting on Windows
- We'll be using CyberChef today.

### What is the KeePass password?
- Search for "Magic" operation in CyberChef, drag that over to the "Recipe" box
- Copy the file name of the file, which is `dGhlZ3JpbmNod2FzaGVyZQ==` (kinda look like base64)
- "BAKE" we got the password: `thegrinchwashere`

### What is the password for ElfServer?
- We go into KeePass, we see a hex password
- Decode `sn0wM4n!` (well use the same "Magic" recipe)

### What is the password for ElfMail?
- `ic3Skating!`
- It looks like ASCII code

### What is the password for Security?
- Well use "From Charcode" from CyberChef with "Comma" and "10" base
- Weird there's a link "hhttps://gist.github.com/heavenraiza/"
- Go there (remove the extra "h")
- Got the flag :)


