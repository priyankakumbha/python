print(48, bin(48))
print(48 >> 1)
# right shift by one
print(48 << 1)
# left shift by one
print(48 >> 2)
print(48 << 2)

# 48 / 2 = 24 + r0
# 24/ 2 = 12 + r0
# 12 / 2 = 6 + r0
# 6/ 2 = 3 + r0
# 3/ 2= 1+ r1
# 1/ 2 = 0 + r1

# bin value for 48 = 00110000 = 16 + 32 = 48
# right shift by one = 00011000 = 8 + 16 = 24
# right shift by 2 = 00001100 = 4 + 8 = 12


# bin value for 48 = 00110000 = 16 + 32 = 48
# left shift by 1 = 01100000 = 32 + 64 = 96
# left shift by 2 = 11000000 = 64 + 128 = 192
