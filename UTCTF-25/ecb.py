from pwn import *

host = 'challenge.utctf.live'
port = 7150

conn = remote(host, port)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-~!?#%&@{}' # 2

# 16 bytes

# block 1
# cracked = 'utflag{'  # 7

# block 2
# cracked = 'utflag{st0p_r0ll' # 16

# block 3
cracked = 'utflag{st0p_r0ll1ng_y0ur_0wn_crypt0' # 32
padding = hex(0x03) * 3

# each block change chksum value, 16 to 32 to 48
# padding is any random valid hex padding
# last part: brute force padding addition to the code

while (True):
    found = False
    conn.recv(1024).decode()
    conn.sendline(godload)
    currCrack = conn.recvline().decode()[66:98]

    for char in chars:
        payload = godload + cracked + char + padding

        chksum = sum(ord(c) for c in payload) % (len(payload)+1)
        totalSum = sum(ord(c) for c in payload)

        if chksum != len(payload):
            newchk = totalSum % (len(payload)+2)
            val = len(payload) + 1 - newchk

            if val == 0:
                val = len(payload) + 1
            payload += chr(val)

        chksum = sum(ord(c) for c in payload) % (len(payload)+1)
        conn.recv(1024).decode()
        conn.sendline(payload.encode())
        testVal = conn.recvline().decode()[66:98]

        if currCrack == testVal:
            cracked += char
            found = True
            break
        
    print("____________________________")
    print(cracked)

    if not found:
        print("fail")
        break

    if len(godload) == 0:
        break
    godload = godload[:-1]

print(cracked)