from pwn import *

host = 'challenge.utctf.live'
port = 7150

conn = remote(host, port)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-~!?#%&@{}' # 2

godload = '\x01' * 8  # 8 bytes
cracked = 'utflag{s'  # 8 bytes
payload = godload + cracked  # Total 16 bytes

# Calculate checksum
chksum = sum(ord(c) for c in payload) % (len(payload) + 1)
totalSum = sum(ord(c) for c in payload)

if chksum < len(payload):
    newchk = totalSum % (len(payload) + 2)
    val = len(payload) + 1 - newchk

    if val == 0:
        val = len(payload) + 1
    payload += chr(val)

print(payload)
payload = payload.encode()

# Simulate connection and sending payload
conn.recv(1024).decode()
conn.sendline(godload)
print(conn.recvline().decode())

conn.recv(1024).decode()
conn.sendline(payload)
print(conn.recvline().decode())
# each block change chksum value, 16 to 32 to 48
# padding is 0 until block 3
# last part: brute force padding addition to the code