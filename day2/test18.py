i = 10
print(i, bin(i))

i = 1
print(i, bin(i))

i  &= 1;
 # i = i & 1
print(i, bin(i))

i = 10
i |= 1;
# i = i | 1
print(i, bin(i))

i = 10
i ^= 1
# i = i ^ 1
print(i, bin(i))

i = 10
i >>= 1
# i= i >>1
print(i, bin(i))

i = 10
i <<= 1
# i = i << 1
print(i, bin(i))

# bin value of 10 : 00001010
# bin value of 1  : 00000001
# &    00000000   numeric value 0
# |    00001011                 11
# ^    00001011                 11
# >>1  00000101                 5
# <<1  00010100                 20
