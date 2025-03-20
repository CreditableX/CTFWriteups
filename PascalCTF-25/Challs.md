# PascalCTF 25

## Introduction
Short 5 hour beginner CTF, did all crypto and some other easier ones. Nothing too difficult, nice practice.

[INDIV]  
Rank: 98/570  
Points: 1313 | base 500

![alt text](cryptofullclear.png)


### Romañs Empyre [50 pts | 354 solves]
My friend Elia forgot how to write, can you help him recover his flag??

We are given this code and an `output.txt` containing the string `TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos`.

```python
import os, random, string

alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
FLAG : str = os.getenv("FLAG")
assert FLAG.startswith("pascalCTF{")
assert FLAG.endswith("}")

def romanize(input_string):
    key = random.randint(1, len(alphabet) - 1)
    result = [""] * len(input_string)
    for i, c in enumerate(input_string):
        result[i] = alphabet[(alphabet.index(c) + key) % len(alphabet)]
    return "".join(result)

if __name__ == "__main__":
    result = romanize(FLAG)
    assert result != FLAG
    with open("output.txt", "w") as f:
        f.write(result)
```

We can see that it is just a caesar cipher and so we solve accordingly.

```python
import random, string

alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"

input_string = "TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos"

def romanize(input_string, key):
    key = random.randint(1, len(alphabet) - 1)
    result = [""] * len(input_string)
    for i, c in enumerate(input_string):
        result[i] = alphabet[(alphabet.index(c) - key) % len(alphabet)]
    return "".join(result)

if __name__ == "__main__":
    for i in range(26):
        print(romanize(input_string, i))
```

<br></br>

### MindBlowing [349 pts | 117 solves]
My friend Marco recently dived into studying bitwise operators, and now he's convinced he's invented pseudorandom numbers! Could you help me figure out his secrets?

We are given this code.

```python
import signal, os

SENTENCES = [
    b"Elia recently passed away, how will we be able to live without a sysadmin?!!?",
    os.urandom(42),
    os.getenv('FLAG', 'pascalCTF{REDACTED}').encode()
]

def generate(seeds: list[int], idx: int) -> list[int]:
    result = []
    if idx < 0 or idx > 2: 
        return result
    encoded = int.from_bytes(SENTENCES[idx], 'big')
    for bet in seeds:
        # why you're using 1s when 0s exist
        if bet.bit_count() > 40:
            continue
        result.append(encoded & bet)
    
    return result

def menu():
    print("Welcome to the italian MindBlowing game!")
    print("1. Generate numbers")
    print("2. Exit")
    print()

    return input('> ')

def handler(signum, frame):
    print("Time's up!")
    exit()

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(300)
    while True:
        choice = menu()

        try:
            if choice == '1':
                idx = int(input('Gimme the index of a sentence: '))
                seeds_num = int(input('Gimme the number of seeds: '))
                seeds = []
                for _ in range(seeds_num):
                    seeds.append(int(input(f'Seed of the number {_+1}: ')))
                print(f"Result: {generate(seeds, idx)}")
            elif choice == '2':
                break
            else:
                print("Wrong choice (。_。)")
        except:
            print("Boh ㄟ( ▔, ▔ )ㄏ")
```

First we see that we have to choose the index of 2 so that we can get `SENTENCES[2]` which has the flag. Afterwards, we also see that we need to input a number larger than 40 bits so that we get a return result of `encoded & bet` from generate. If we manage to submit a number that is equivalent to `0b111111...`, the result will simply be `encoded` (read up on `&` operator if unsure why), which is (some part of) the encoded flag. 

Trying a 40-bit number only gives the last 5 chars of the flag as 8 bits correspond to 1 ASCII character. So, we try to put more 1s, but the system rejects it and returns `result=[]` for many of the cases. Additionally, there is a comment saying `why you're using 1s when 0s exist`, which gives us more hints.

Our finals solution is to then add 40 x `0` to the back of our original number, giving us `0b11111...0000...`. What this does is that we get the next 5 chars of the flag from the back, using the same idea as before. We trial the number of loops until we get the full flag displayed.

```python
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
```
  
<br></br>

### My favourite number [460 pts | 61 solves]
Alice and Bob are playing a fun game, can you guess Alice's favourite number too?

We are given this code, and a text file which has all the message encrypted based on `sendToAlice` and `sendToBob`.

```python
e = 65537

alice_p, alice_q = getPrime(1024), getPrime(1024)
alice_n = alice_p * alice_q

print(f"hi, i'm Alice, my public parameters are:\nn={alice_n}\ne={e}")

def sendToAlice(msg):
    pt = bytes_to_long(msg.encode())
    assert pt < alice_n
    ct = pow(pt, e, alice_n)
    print(f"bob: {ct}")

bob_p, bob_q = getPrime(1024), getPrime(1024)
bob_n = bob_p * bob_q

print(f"hi Alice! i'm Bob, my public parameters are:\nn={bob_n}\ne={e}")

def sendToBob(msg):
    pt = bytes_to_long(msg.encode())
    assert pt < bob_n
    ct = pow(pt, e, bob_n)
    print(f"alice: {ct}")


alice_favourite_number = bytes_to_long(FLAG.encode())
assert alice_favourite_number < 2**500

sendToBob("let's play a game, you have to guess my favourite number")

upperbound = 2**501
lowerbound = 0
while upperbound - lowerbound > 1:
    mid = (upperbound + lowerbound) // 2
    sendToAlice(f"Is your number greater than {mid}?")
    if alice_favourite_number > mid:
        sendToBob(f"Yes!, my number is greater than {mid}")
        lowerbound = mid
    else:
        sendToBob(f"No!, my number is lower or equal to {mid}")
        upperbound = mid

sendToAlice(f"so your number is {upperbound}?")
assert upperbound == alice_favourite_number
sendToBob("yes it is!")
sendToAlice("that's a pretty cool number")
```

Since we know that the sending functions are deterministic, and we know the values of `e`, `bob_n` and `alice_n`, we can try to recreate the message sent in each line. Essentially, we can follow the logic of binary search, and craft the encoded message of our own. Since there are only 2 messages that each step can take (either `Yes!, my number...` or `No!, my number...`), we can easily know what step next to take in the binary search.

At the end, we decode from long to bytes alice's flag.

```python
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import re

isAlice = True
upperbound = 2**501
lowerbound = 0

alice_n = 1707...SNIP...2249 # truncated
bob_n = 24013931...SNIP...30313 # truncated
e = 65537

def sendToAlice(msg):
    pt = bytes_to_long(msg.encode())
    return pow(pt, e, alice_n)

def sendToBob(msg):
    pt = bytes_to_long(msg.encode())
    return pow(pt, e, bob_n)

with open("favoutput.txt", "r") as f:
    for line in f:
        line = line.strip()
        
        if isAlice:
            number_match = re.search(r"\d+", line)
            if number_match:
                line_number = int(number_match.group())
            else:
                print("Error: No number found in line:", line)
                continue

            number = (upperbound + lowerbound) // 2
            output1 = sendToBob(f"Yes!, my number is greater than {number}")
            output2 = sendToBob(f"No!, my number is lower or equal to {number}")

            if line_number == output1:
                print("UP")
                lowerbound = number
            elif line_number == output2:
                print("DOWN")
                upperbound = number
            else:
                print(f"Unexpected output: {line_number}")
                exit()
                
        isAlice = not isAlice
    print("final number ", long_to_bytes(number))
```