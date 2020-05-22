def my_generator():
	print('stage1')
	yield 1
	print('stage2')
	yield 10
	print('stage3')
	yield 'abc'

g1 = my_generator()

print(next(g1));
print('-----')
print(next(g1));
print('-----')
print(next(g1));
print('-----')
