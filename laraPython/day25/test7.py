'''
1
1 1
1 0 1
1 0 0 1
1 0 0 0 1
1 0 0 0 0 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1 1


'''

for row in range(1, 9):
	for col in range(1, row + 1):
		if (row == 1 or row == 8 or col == 1 or col == row):
			print(1, ' ', end='')
		else:
			print(0, ' ', end='')
	print();