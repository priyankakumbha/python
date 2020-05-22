'''

9
8 8
7 7 7 
6 6 6 6
5 5 5 5 5
4 4 4 4 4 4
3 3 3 3 3 3 3
2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1

'''

for row in range(9, 0, -1):
	for col in range(9, row - 1, -1):
		print(row, ' ', end='')
	print()