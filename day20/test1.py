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

for element in my_generator():
	print(element)
