'''
# example of decorator
def sampleDecorator(func):
    def addingFunction():
        # some new statments or flow control
        print("This is the added text to the actual function.")
        # calling the function
        func()

    return addingFunction


@sampleDecorator
def actualFunction():
    print("This is the actual function.")


actualFunction()


def d1():
	print("done")


d2 =sampleDecorator(d1)
d2()

'''


'''
def dec(f1):
	def m1(a):
		print(1, a)
		f1(a)
		print(3)
	return m1
@dec
def d1(x):
	print("p", x)



d1(10)
'''

'''
def dec1(func):
	def o1(a, b):
		print(1, a, b)
		func(a, b)
		print(2, a, b)
	return o1

@dec1
def f1(a, b):
	print(3, a, b)


f1(10, 20)
'''
'''
def dec1(func):
	def hello(v1):
		print(2, v1)
		if v1 <= 5:
			print("some thing")
			return;
		func(v1)
		print(2, v1)
	return hello;

@dec1
def myFunc(a):
	print(3, a)


myFunc(2)
'''
'''
class A:
	def __init__(self, f1):
		self.f1 = f1

	def __call__(self):
		print(1)
		self.f1()
		print(2)
	
@A
def f1():
	print(3)


f1()

'''


'''
class A:
	def __init__(self, f1):
		self.f1 = f1

	def __call__(self):
		print(1)
		self.f1()
		print(2)
	
@A
def f1():
	print(3)


f1()

'''
'''
class A:
	def __init__(self, f1):
		self.f1 = f1

	def __call__(self, a):
		print(1, a)
		self.f1(a)
		print(2, a)
	
@A
def f1(a):
	print(3, a)


f1(20)

'''

'''
def v1():
	yield 1
	yield 2
	yield 3
	yield 4
g1 = v1();
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))

'''
'''
def v1():
	yield 1
	yield 2
	yield 3
	yield 4

g1 = v1()
print(type(g1))
'''

def c1(n):
	i = 0;
	while(i <= n):
		yield i
		i = i + 2

g1 = c1(10)
for i in c1(20):
	print(i)















