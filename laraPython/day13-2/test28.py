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
a1.i = 6000
a1.test1()
a2.test1()
a3.test1()
a2.i = 'abc'
a1.test1()
a2.test1()
a3.test1()
a3.i = 'test'
a1.test1()
a2.test1()
a3.test1()

