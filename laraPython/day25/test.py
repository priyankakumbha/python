'''

A
B A
C B A
D C B A
E D C B A
F E D C B A
G F E D C B A
H G F E D C B A
I H G F E D C B A
'''

base_char = 'A'

for row in range(0, 9):
	for col in range(row, -1, -1):
		print(chr(ord(char) + col), ' ', end='')
	print()