# [Web Exploit] SQL Injection stuff

Advent of Cyber 2: https://github.com/rcs-tringuyen/tryhackme_christmas

IP: 10.10.99.195:8000

### Without using directory brute forcing, what's Santa's secret login panel?
- `/santapanel`

### Visit Santa's secret login panel and bypass the login using SQLi
- Well I tried sqlmap it but it seems like too many request broke the page.
- So I went on https://github.com/payloadbox/sql-injection-payload-list in the "SQL Injection Auth Bypass Payloads", tried some of them and this one works: `admin' or '1'='1`

### How many entries in the Gift database?
- Same stuff on the github page, but the "Generic" section.
- `' OR '1`

### Paul ask for?
- `github ownership`

### Flag
- First the data is "sqlite" because the Santa's TODO said so!
- Secondly we need to capture the request since we need the session cookies!
- `sqlmap -r day5_burp --batch --dump-all --tamper=space2comment --dbms=sqlite`
- FLAG!!

### Admin Password
- It's there once you cracked the database ;)
