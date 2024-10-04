import random
import os

def xor_func(msg, key):
    return bytes(a ^ b for a, b in zip(msg, key))

def encrypt(keys, msg):
    result = msg
    for key in keys:
        result = xor_func(result, key)
    return result

if __name__ == "__main__":
    msg = "CS2107{REDACTED}"
    msg = msg.encode()
    key_length = len(msg)
    key1 = random.randbytes(key_length)
    key2 = os.urandom(key_length)
    key3 = b'o' * key_length
    key4 = bytes([random.randint(0, 255) for _ in range(len(msg))])
    key5 = random.randbytes(key_length)
    key6 = os.urandom(key_length) 

    keys = [key1, key2, key3, key4, key5, key6]
    enc_msg = encrypt(keys, msg)
    keys = [bytes.fromhex("984b1852b99a092e4ce4dd01fd6e47962f3523ee3c95bd"), 
            bytes.fromhex("fac829ad1b66ccc24fcbda8e0bbc46133429f70e5b669e"),
            bytes.fromhex("6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f"),
            bytes.fromhex("f2bb87644b62bc3d531a3b9b0f853335093df5c49fd27c"),
            bytes.fromhex("2765d2d7cb67cf7ccd41d2675f89cb121b1bd2667b76d8"), 
            bytes.fromhex("8159c60734ae7e095fe5dffc1302abab5a37f34a0ee0fe") ]
    dec_msg = encrypt(keys, bytes.fromhex("1a38ff15490fdc939dac018d9ad70e390f221c1ec3f96b"))
    print(dec_msg)

    print(f'key1 = "{key1.hex()}"')
    print(f'key2 = "{key2.hex()}"')
    print(f'key3 = "{key3.hex()}"')
    print(f'key4 = "{key4.hex()}"')
    print(f'key5 = "{key5.hex()}"')
    print(f'key6 = "{key6.hex()}"')
    print(f'Secret = "{enc_msg.hex()}"')
    
# Keys used to generate the flag

# key1 = "984b1852b99a092e4ce4dd01fd6e47962f3523ee3c95bd"
# key2 = "fac829ad1b66ccc24fcbda8e0bbc46133429f70e5b669e"
# key3 = "6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f6f"
# key4 = "f2bb87644b62bc3d531a3b9b0f853335093df5c49fd27c"
# key5 = "2765d2d7cb67cf7ccd41d2675f89cb121b1bd2667b76d8"
# key6 = "8159c60734ae7e095fe5dffc1302abab5a37f34a0ee0fe"
# Secret = "1a38ff15490fdc939dac018d9ad70e390f221c1ec3f96b"