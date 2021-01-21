# [Network] Wireshark

### Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
- `10.11.3.2`

### If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?
- `http.request.method == GET`

### Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?
- Apply filter `ip.src == 10.10.67.199`
- `10.10.15.52`
- You will find link `/posts/<your answer here>` in the info section

### Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?
- `plaintext_password_fiasco` Sorting by FTP

### Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?
- SSH

### Analyse "pcap3.pcap" and recover Christmas! What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?
- Export the HTTP protocol to files
- Unzip the attachment
