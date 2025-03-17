from pwn import *

host = 'challenge.utctf.live'
port = 7150

conn = remote(host, port)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-~!?#%&@{}' # 2

# 32 hex 


godload = '\x01' * 8 # 16

cracked = 'utflag{'  # 14
#cracked = 'utflag{st0p_r0ll' # 32
#cracked = 'utflag{st0p_r0ll1ng_y0ur_0wn_cry' # 64
#cracked = 'utflag{st0p_r0ll1ng_y0ur_0wn_crypt0qb' # 74 
#cracked = 'utflag{st0p_r0ll1ng_y0ur_0wn_crypt0' # 70
randomVals = ''
padding = ''
# padding = hex(0x02) * 2

# each block change chksum value, 16 to 32 to 48
# padding is 0 until block 3
# last part: brute force padding addition to the code

while (True):
    found = False
    conn.recv(1024).decode()
    conn.sendline(godload)
    currCrack = conn.recvline().decode()[2:34]
    print("godload gives " + currCrack)

    for char in chars:
        payload = godload + cracked + char + padding
        # payload = godload.encode() + cracked.encode() + char.encode() + padding.encode()

        chksum = sum(ord(c) for c in payload) % (len(payload)+1)
        totalSum = sum(ord(c) for c in payload)

        if chksum <= 16:
            newchk = sum(ord(c) for c in payload) % (len(payload)+2)
            val = len(payload) + 1 - newchk

            if val == 0:
                val = len(payload) + 1
            # payload = payload.encode() + chr(val).encode()
            print(val)
            payload += chr(val)
        # print(f"Payload length: {len(payload)}")

        chksum = sum(ord(c) for c in payload) % (len(payload)+1)
        print(chksum)
        conn.recv(1024).decode()
        conn.sendline(payload.encode())
        testVal = conn.recvline().decode()[2:34]

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