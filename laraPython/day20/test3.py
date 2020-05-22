def my_generator():
	print('a')
	yield 1

def f1():
	print('a')

def f2():
	print('a')
	return 100

print(type(my_generator))
print(type(f1))
print(type(f2))
print(type(my_generator()))
print(type(f1()))
print(type(f2()))
