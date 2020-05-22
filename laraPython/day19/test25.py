class MyDec:
	def __init__(self, f1):
		self.f1 = f1
	def __call__(self, *arg1):
		print(1, arg1)
		self.f1(*arg1)
		print(2, arg1)

@MyDec
def function0():
	print("i am from function0:")


@MyDec
def function1(a):
	print("i am from function1:", a)

@MyDec
def function2(a, b):
	print("i am from function1:", a, b)

@MyDec
def function3(a, b, c):
	print("i am from function1:", a, b, c)

function0();
print("-------")
function1('abc');
print("-------")
function2(True, 123);
print("-------")
function3(True, 123, 'abc');


