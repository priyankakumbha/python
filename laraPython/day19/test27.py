class Decorator:
	def __init__(self, f1):
		self.f1 = f1
	def __call__(self, *args):
		print("pre processing", *args)
		i = self.f1(*args)
		print("post processing", *args)
		return i

@Decorator
def myFunction(a1, a2):
	print("from my function", a1, a2)
	return 'abc'

print(myFunction(12, 'abc'))
