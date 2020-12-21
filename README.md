# [Special by TheCyberMentor] OSINT

- Hunt for information using the limited infomation.
- **[Web] Username searching**: https://namechk.com/, https://whatsmyname.app/, https://namecheckup.com/
- **[Tool] Username searching**: https://github.com/WebBreacher/WhatsMyName, https://github.com/sherlock-project/sherlock

## Task 1:
- Username: *IGuidetheClaus2020*

### What URL will take me directly to Rudolph's Reddit comment history:
- Using namechk.com to search for Reddit name
- `https://www.reddit.com/user/IGuidetheClaus2020/comments/`

### According to Rudolph, where was he born?
- `Chicago` (By browsing the comment history)

### Rudolph mentions Robert.  Can you use Google to tell me Robert's last name?
- Actually search `Rudolph chicago robert`
- `Robert L. May`

### On what other social media platform might Rudolph have an account?
- `twitter`
- `IGuideClaus2020`

## Task 2:
- This task was created to identify common critical steps in an OSINT investigation. Reverse image searching can help not only identify where an image was taken, but it can assist with identifying websites where that photo exists as well as similar photos (possibly from the same photoset), which can be incredibly useful in an investigation. While Google Images is used in our example, other sites should also be utilized to be as thorough as possible. No one site is perfect when it comes to reverse image searching (or any tool for that matter). Sites like https://yandex.com/images/ , https://tineye.com/ and https://www.bing.com/visualsearch?FORM=ILPVIS are great as well. Additionally, do not neglect the possibility of EXIF data existing in an image. While a lot of sites strip this data, not all do. It never hurts to look and can provide a wealth of information when the data is still there.

- Finally, breached data can be incredibly useful from an investigative standpoint. Breach data does not just include passwords. It often has full names, addresses, IP information, password hashes, and more. We can often use this information to tie to other accounts. For example, say we find an account with the email of v3ry1337h4ck3r@gmail.com. If we search that email for breached data, we might find a password or hash associated with it. If unique enough, we can search that password or hash in a breach database and use it to identify other possible accounts. We can do the same with usernames, IPs, names, etc. The possibilities are vast and one email address can lead to a slew of information.

- Websites such as https://haveibeenpwned.com/ will help identify if an account has ever been breached and will, at a minimum, inform us if an account existed at one point. However, it does not provide any password information. Free sites such as http://scylla.sh/ will provide password information and are easy to search through. The data on free sites can tend to be older and not up to date with the latest breach information, but these sites are still a powerful resource. Lastly, paid sites such as https://dehashed.com/ offer up to date information and are easily searchable at affordable rates.

### Rudolph's favorite TV show right now?
- `bachelorette`

### Where did Rudolph's parade happened?
- Used vandex.com/image to reverse search Rudolph's image. It's `Chicago`

### Extract the metadata from the picture?
- You could use some tools but I'm too lazy so I used online EXIF @ http://metapicz.com/#landing
- `41.891815 N, 87.624277 W`
- `{FLAG}ALWAYSCHECKTHEEXIFD4T4`

### PWNED Rudolph's email T_T
- Used https://scylla.sh/ with `email:rudolphthered@hotmail.com`
- `spygame`

### Street number of Rudolph's current hotel
- Search for nearby hotel close to the coordinates.
- `540`


