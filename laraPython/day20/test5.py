def my_generator():
	print('i am from my_generator')
	yield 1

def f1():
	print('i am from f1')

def f2():
	print('i am from f2')
	return 100

next(my_generator());
print('-----')
f1();
print('-----')
f2();
print('-----')