'''
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G

'''

'''
char = 'A';
print(char)					# A
print(chr(ord(char) + 1) )	# B
print(chr(ord(char) + 2) )	# C
print(chr(ord(char) + 3) )	# D

ch = 'f'
print(chr(ord(ch) + 1)) #g
print(chr(ord(ch) + 2))	#h
print(chr(ord(ch) + 3))	#i
print(chr(ord(ch) + 5))	#k
'''

from_char = 'A'
for row in range(0, 7):
	for col in range(0, row + 1):
		print(chr(ord(from_char) + row), ' ', end='')
	print()




