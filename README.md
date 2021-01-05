# [Blue Team] Powershell Cont.

IP: 10.10.173.57

Advent of Cyber 2: 

- Reminder how to start Remmina (RDP on Linux): `snap run remmina`

### Read the contents of the text file within the Documents folder. What is the file hash for db.exe?
- 596690FFC54AB6101932856E6A78E3A1

### What is the file hash of the mysterious executable within the Documents folder?
- `Get-FileHash -Algorithm MD5 deebee.exe`
- Hash: `5F037501FB542AD2D9B06EB12AED09F0`

### What is the flag hidden in the executable?
- `c:\Tools\strings64.exe -accepteula deebee.exe`
- Flag: `THM{f6187e6cbeb1214139ef313e108cb6f9}`

### What is the flag that is displayed when you run the database connector file?
- First you run `Get-Item -Path deebee.exe -Stream *` to find all the executable's stream.
- There is one call "DATA" and another call "hidedb"
- `wmic porocess call create $(Resolve-Path deebee.exe:hidedb)`
- Found the flag:) THM{088731ddc7b9fdeccaed982b07c297c}
