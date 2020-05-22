class Decorator:
	def __init__(self, f1):
		self.f1 = f1
	def __call__(self):
		print("pre processing")
		i = self.f1()
		print("post processing")
		return i

@Decorator
def myFunction():
	print("from my function")
	return 'abc'

print(myFunction())
