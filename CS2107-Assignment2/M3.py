from z3 import *

conditions = [
        "(flag[16] - flag[14] + (flag[0] ^ flag[11]) + (flag[0] ^ flag[14]) + flag[13] - flag[19] == 67) ",
        "(flag[19] + flag[10] + flag[10] + flag[19] + flag[0] - flag[20] + flag[3] - flag[18] == 362) ",
        "(flag[0] - flag[15] + flag[20] + flag[18] == 151) ",
        "(flag[13] - flag[8] + flag[10] - flag[20] + flag[3] - flag[17] == 16) ",
        "(flag[3] - flag[17] + flag[19] + flag[4] + (flag[12] ^ flag[17]) + flag[10] - flag[2] == 240) ",
        "(flag[11] - flag[21] + flag[12] - flag[10] == 99) ",
        "((flag[18] ^ flag[19]) + flag[6] - flag[16] + (flag[5] ^ flag[16]) == 100) ",
        "(flag[6] - flag[13] + (flag[10] ^ flag[15]) + flag[21] - flag[5] == 65) ",
        "((flag[5] ^ flag[3]) + flag[12] - flag[11] + (flag[6] ^ flag[4]) == 173) ",
        "(flag[6] - flag[14] + flag[9] - flag[2] + flag[8] - flag[15] + flag[21] - flag[11] == -11) ",
        "(flag[12] - flag[17] + flag[12] + flag[8] == 276) ",
        "(flag[10] + flag[21] + (flag[19] ^ flag[2]) == 159) ",
        "((flag[5] ^ flag[16]) + flag[16] + flag[3] + (flag[0] ^ flag[16]) == 227) ",
        "(flag[10] + flag[3] + flag[3] - flag[19] + (flag[19] ^ flag[0]) == 79) ",
        "(flag[10] - flag[8] + flag[2] - flag[19] == -49) ",
        "(flag[17] - flag[1] + flag[4] + flag[11] + flag[17] - flag[9] == 151) ",
        "(flag[14] + flag[10] + flag[18] - flag[9] + flag[5] + flag[10] == 279) ",
        "(flag[5] - flag[16] + flag[8] - flag[12] + flag[17] - flag[13] + flag[11] - flag[2] + flag[1] + flag[21] == 13) ",
        "((flag[19] ^ flag[13]) + flag[6] - flag[13] + flag[17] - flag[11] + (flag[16] ^ flag[12]) == 70) ",
        "(flag[4] - flag[16] + (flag[2] ^ flag[7]) == 16) ",
        "(flag[8] - flag[17] + flag[14] - flag[3] + (flag[8] ^ flag[14]) + flag[5] + flag[1] + flag[7] + flag[10] == 440) ",
        "(flag[4] - flag[0] + flag[2] - flag[4] + flag[15] - flag[21] + flag[17] + flag[2] == 152) ",
        "(flag[5] - flag[18] + flag[17] - flag[4] + flag[15] + flag[2] + flag[21] - flag[18] + flag[7] + flag[6] == 299) ",
        "(flag[21] - flag[19] + flag[7] - flag[18] + flag[16] - flag[21] + (flag[12] ^ flag[18]) == 74) ",
        "((flag[10] ^ flag[2]) + flag[2] + flag[7] + flag[20] + flag[13] + (flag[3] ^ flag[16]) + flag[9] + flag[6] == 715) ",
        "(flag[8] - flag[3] + (flag[14] ^ flag[2]) + flag[11] + flag[0] + flag[1] - flag[19] == 259) ",
        "(flag[19] - flag[7] + flag[0] + flag[16] + flag[11] + flag[17] == 372)" ]

flag = [BitVec(f'arr[{i}]', 9) for i in range(22)]
    
s = Solver()

for i in conditions:
    s.add(eval(i))

print(s.check())
print(s.model())

arr = [0] * 22

arr[1] = 51
arr[15] = 82
arr[19] = 100
arr[14] = 102
arr[17] = 51
arr[12] = 116
arr[13] = 95
arr[9] = 98
arr[20] = 33
arr[2] = 95
arr[18] = 78
arr[7] = 89
arr[21] = 49
arr[16] = 105
arr[5] = 95
arr[4] = 115
arr[3] = 49
arr[11] = 83
arr[8] = 95
arr[0] = 122
arr[10] = 51
arr[6] = 109

for i in arr:
    print(chr(i), end="")