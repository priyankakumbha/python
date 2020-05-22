class A:
	def __init__(self, p1 = 0):
		self.x = p1;

	def __add__(self, obj1):
		obj = A();
		obj.x = self.x + obj1.x
		return obj

a1 = A(10)
a2 = A(20)
a3 = a1 + a2

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
