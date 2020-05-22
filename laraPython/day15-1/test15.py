class A:
	def __add__(self, obj1):
		y = self.x + obj1.x
		return y

a1 = A()
a1.x = 10;
a2 = A()
a2.x = 20;
a3 = A();
a3.x = a1 + a2

print(a3.__dict__)
