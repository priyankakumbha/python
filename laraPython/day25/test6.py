'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1
7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1

'''

for row in range (1, 10):
	for col in range(row, 0, -1):
		print(col, ' ', end='')
	print();