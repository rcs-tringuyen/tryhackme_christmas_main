# [Special by Tib3rius] Server-Side Request Forgery (SSRF)

IP: 10.10.177.211

Advent of Cyber 2: 

## Walkthrough

1) Go to http://10.10.177.211

2) Enter some name in the search bar. The link will be like: http://10.10.177.211/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3Dname. URL decode the `proxy` part it will something like: http://list.hohoho:8080/search.php?name=name. Can also use the script linked: `. ./urldecoder.sh && urldecode <link>`

3) 



