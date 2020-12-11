# [Network] Nmap

IP: 10.10.82.120

Advent of Christmas: https://github.com/rcs-tringuyen/tryhackme_christmas

### When was Snort created?
- You just have to google. It's 1998

### Using Nmap on 10.10.82.120 , what are the port numbers of the three services running? 
- `nmap 10.10.82.120 | tee nmap_initial_scan.txt`
- 80, 2222, 3389

### What Linux distribution the server is running?
- `nmap -A -sV 10.10.82.120`
- ubuntu

### Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?\
- https://nmap.org/nsedoc/scripts/http-title.html
- `nmap --script http-title 10.10.82.120`
- Blog

### Other vulnerabilities?
- Try this room out https://tryhackme.com/room/blue