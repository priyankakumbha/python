class A:
	def __init__(self):
		self.i = 10
		self.j = 40;
		self.k = 'hello'
a1 = A()
print(a1.__dict__)
a2 = A()
print(a2.__dict__)
a3 = A()
print(a3.__dict__)
a1.i = 6000
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
a2.i = 'abc'
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
a3.i = 'test'
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
