from pwn import *

if __name__ == "__main__":
    port = 420
    host = 'mindblowing.challs.pascalctf.it'

    conn = remote(host, port)
    num = 0b1111111111111111111111111111111111111111
    answer = ''
    print("here")

    def int_to_ascii(n):
        byte_array = n.to_bytes((n.bit_length() + 7) // 8, 'big')
        return ''.join(chr(b) for b in byte_array) 

    for i in range(15):
        conn.sendline("1".encode())
        conn.sendline("2".encode())
        conn.sendline("1".encode())
        conn.sendline(str(num).encode())
        data = conn.recvuntil(b']').decode()
        data = data[data.find("[") + 1 : data.find("]")]
        ascii_chars = int_to_ascii(int(data)).rstrip('\x00')
        print(ascii_chars)
        answer = ascii_chars + answer
        num = num << 40
        
    print(answer)