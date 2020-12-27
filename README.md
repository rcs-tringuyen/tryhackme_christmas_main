# [Special by Tib3rius] Server-Side Request Forgery (SSRF)

IP: 10.10.177.211

Advent of Cyber 2: 

## Walkthrough

1) Go to http://10.10.177.211

2) Enter some name in the search bar. The link will be like: http://10.10.177.211/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3Dname. URL decode the `proxy` part it will something like: http://list.hohoho:8080/search.php?name=name. Can also use the script linked: `. ./urldecoder.sh && urldecode <link>`

3) Try fetching the root folder http://10.10.177.211/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2F which return 404. 

4) Trying with port 22. http://10.10.177.211/?proxy=http%3A%2F%2Flist.hohoho%3A22. Error ` Recv failure: Connection reset by peer `. Promising and we'll find another way!

5) Another thing we can try to do with SSRF is access services running locally on the server. We can do this by replacing the list.hohoho hostname with "localhost" or "127.0.0.1" (among others). Try this now: http://10.10.177.211/?proxy=http%3A%2F%2Flocalhost .Oops! It looks like the developer has a check in place for this, as the message returned says "Your search has been blocked by our security team." Indeed, if you try other hostnames (e.g. 127.0.0.1, example.com, etc.) they will all be blocked. The developer has implemented a check to ensure that the hostname provided starts with "list.hohoho", and will block any hostnames that don't.

6) As it turns out, this check can easily be bypassed. Since the hostname simply needs to start with "list.hohoho", we can take advantage of DNS subdomains and create our own domain "list.hohoho.evilsite.com" which resolves to 127.0.0.1. In fact, we don't even need to buy a domain or configure the DNS, because multiple domains already exist that let us do this. The one we will be using is localtest.me, which resolves every subdomain to 127.0.0.1. We can therefore set the hostname in the URL to "list.hohoho.localtest.me", bypass the check, and access local services: http://10.10.177.211/?proxy=http%3A%2F%2Flist.hohoho.localtest.me. Success! It appears that there is a web server running locally, and it has a message from Elf McSkidy that contains some sensitive information we can use!

7) Login with username `Santa`, password: `Be good for goodness sake!`


