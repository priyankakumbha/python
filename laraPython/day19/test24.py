class MyDec:
	def __init__(self, f1):
		self.f1 = f1
	def __call__(self, arg1, arg2):
		print(1, arg1, arg2)
		self.f1(arg1, arg2)
		print(2, arg1, arg2)

@MyDec
def function1(a, b):
	print("i am from function1:", a, b)

function1('abc', 345);
print("-------")
function1(True, 123);


