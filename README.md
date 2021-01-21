# [Web Exploitation] Chirstmas Chaos

IP: http://10.10.87.93

### What's the flag
- This challenge shows you how to brute force login form with BurpSuite.
- First, intercept the login info with Burp.
- Send to intruder.
- Start a "Cluster Bomb" attack
- Pass in the wordlist for payload 1 (username) and payload 2 (password)
- Username/Password combination provided are
- Username: root, user, admin
- Password: root, password, 12345
- Then you would use the combination which has the different length (since successful login has a different length then all the fail ones).
- FLAG :D
