class MyDec:
	def __init__(self, f1):
		self.f1 = f1
	def __call__(self, arg1):
		print(1, arg1)
		self.f1(arg1)
		print(2, arg1)

@MyDec
def function1(arg1):
	print("i am from function1:", arg1)

function1('abc');
print("-------")
function1(123);


