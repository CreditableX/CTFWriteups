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