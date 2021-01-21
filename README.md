# [Blue Team] Power Shell

IP: 10.10.100.71

Advent of Cyber 2: 

## Walkthrough:
- First we SSH into the IP: `ssh 10.10.100.71 -l mceager`, password `r0ckStar!`
- Launch `PowerShell` in the cmd
- `Set-Location .\Documents\`

### Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?
- `Get-ChildItem -File -Hidden -ErrorAction SilentlyContinue`
- `Get-Content -Path e1fone.txt`

### Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?
- `Set-Location -Path C:\Users\mceager\desktop`
- `Get-ChildItem -Directory -Hidden -ErrorAction SilentlyContinue`
- `Set-Location .\elf2wo\`
- `Get-Content e70smsW10Y4k.txt`

### Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)
- `Set-Location -Path C:\Windows`
- `Get-ChildItem -Directory -Hidden -ErrorAction SilentlyContinue -Filter '*3*' -Recurse` which found the folder `3lfthr3e` in C:\Windows\System32

### How many words does the first file contain?
- `Get-Content 1.txt | Measure-Object -Word`
- 9999

### What 2 words are at index 551 and 6991 in the first file?
- `(Get-Content 1.txt)[551]`
- `(Get-Content 1.txt)[6991]`

### This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)
- `Select-String 2.txt -Pattern 'redryder'` will return `2.txt:558704:redryderbbgun`
- Answer is `red ryder bb gun`
