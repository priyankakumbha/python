class MyDecorator: 
	def __init__(self, function): 
		self.function = function 
	
	def __call__(self, *args): 
		print(1)
		i = self.function(*args) 
		print(2)
		return i;

@MyDecorator
def function(name, message): 
	print(name, message) 
	return 200;

@MyDecorator
def function1(name, message, test): 
	print(name, message, test) 
	return 'abc';

@MyDecorator
def function2(test): 
	print(test) 
	return True;

print(function("abc", "hello"))
print(function1("abc", "hello", "hi")) 
print(function2("abc")) 

def f4():
	print("f4")
	return 567
m1 = MyDecorator(f4)
print(m1())
