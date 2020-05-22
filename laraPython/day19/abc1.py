class MyDecorator: 
	def __init__(self, function): 
		self.function = function 
	
	def __call__(self, *args): 
		print(1)
		self.function(*args) 
		print(2)

@MyDecorator
def function(name, message): 
	print(name, message) 

@MyDecorator
def function1(name, message, test): 
	print(name, message, test) 

@MyDecorator
def function2(test): 
	print(test) 

function("abc", "hello") 
function1("abc", "hello", "hi") 
function2("abc") 

def f4():
	print("f4")

m1 = MyDecorator(f4)
m1()
