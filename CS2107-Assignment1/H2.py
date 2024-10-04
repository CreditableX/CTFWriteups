from pwn import *
import random
from mt19937predictor import MT19937Predictor

p = remote("cs2107-challs.nusgreyhats.org", 5051)

predictor = MT19937Predictor()

# running 624 times for mersenne-twister prediciton
for _ in range(624):
    p.recvline()
    guess = (random.getrandbits(32))
    p.sendline(str(guess).encode())
    # print(guess)
    response = p.recvxine().strip()[15:]
    predictor.setrandbits(int(response.decode()), 32)
    # print(response.decode())


# fast break the next input
guess = predictor.getrandbits(32)
p.recvline()
p.sendline(str(guess).encode())
response = p.recvline().strip()
print(response.decode())
p.close()




