# [Reverse Engineering] Getting started

IP: 10.10.84.215

Resources for r2: https://scoding.de/uploads/r2_cs.pdf

First we `ssh 10.10.84.215 -l elfmceager`, password: `adventofcbyer`

`r2 -d ./challenge1`
`aa`
`alf | grep main`
`pdf @main`
`db 0x00400b58`
`px @rbp-0xc`

### What is the value of local_ch when its corresponding movl instruction is called (first if multiple)?
- `1` 

### What is the value of eax when the imull instruction is called?
- Because `imul` is trying to multiply an int, instead of seeing the value of `eax`, we observe from `local_8h` (addr: `rbp-0x8`)
- `db 0x00400b62`
- `px @rbp-0x8`

### What is the value of local_4h before eax is set to 0?
- `db 0x00400b66`
- `px @rbp-0x4`
- The answer is also 6

