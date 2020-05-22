i = 150
print(i, bin(i))
# i = 2
# print(i, bin(i))
i  &= 2;
 # i = i & 1
print(i, bin(i))

i = 150
i |= 2;
# i = i | 1
print(i, bin(i))

i = 150
i ^= 2
# i = i ^ 1
print(i, bin(i))

i = 150
i >>= 2
# i= i >>1
print(i, bin(i))

i = 150
i <<= 2
# i = i << 1
print(i, bin(i))


# bin value of 150 : 0010010110
# 150/ 2 = 75 + r0
# 75/ 2 = 37 + r1
# 37 / 2 = 18 + r1
# 18 / 2= 9 + r0
# 9 / 2 = 4 + r1
# 4/ 2 = 2 + r0
# 2 / 2 = 1+ r0
# 1/ 2= 0 + r1
# bin value of 2  :  0b00000010
# &     0000000010    2
# |     0010010110  150
# ^       0010010100  148
# >>2       00100101   37
# <<2       10010110
