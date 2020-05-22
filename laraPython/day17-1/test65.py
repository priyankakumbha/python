class A:
	def __init__(self, param):
		self.param = param

	def __str__(self):
		return self.param



a1 = A("hello")
print(a1)