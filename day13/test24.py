class A:
	def test1(self):
		print(self.i);


a1 = A()
a1.i = 10;
a1.j = 'abc'
a1.test1()

a2 = A();
a2.i = 200
a2.k = 500;
a2.test1()

print(a1.j, a2.k)
