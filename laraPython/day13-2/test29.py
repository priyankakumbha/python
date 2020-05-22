class A:
	def __init__(self):
		self.i = 10
		self.j = 40;
		self.k = 'hello'
	def test1(self):
		print(self.i, self.j, self.k)
a1 = A()
a1.test1()
a2 = A()
a2.test1()
a3 = A()
a3.test1()
a1.m = 'hello'
a2.p = 'test'
a3.c = 3.5;
a1.test1()
a2.test1()
a3.test1()

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

