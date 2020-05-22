def my_generator():
	print('a')
	yield 1
	print('b')
	yield 2
	print('c')
	yield 3
	print('d')
	yield 4
	print('end')

g1 = my_generator()

for element in g1:
	print(element)
