'''
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
'''


base_char = 'A'

for row in range(0, 8):
	for col in range(0, row + 1):
		print(chr(ord(base_char) + col), ' ', end='')
	print()