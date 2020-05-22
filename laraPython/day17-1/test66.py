class A:
	def __init__(self, param1, param2):
		self.param1 = param1
		self.param2 = param2

	def __str__(self):
		return "object state(content):" + self.param1 + ", " + self.param2



a1 = A("hello", "xyz")
print(a1)