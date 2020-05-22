class A:
	def f1(self, i):
		print("from f1")
		self.i = i;

	def f2(self, m):
		print("from f2")
		self.j = m


a1 = A();
print(a1.__dict__)
a1.f1(10)
print(a1.__dict__)
a1.f2(20)
print(a1.__dict__)