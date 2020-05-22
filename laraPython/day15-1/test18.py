class A:
	def __init__(self, p1 = 0, p2 = 0):
		self.x = p1;
		self.y = p2;

	def __add__(self, rightOperand):
		obj = A();
		obj.x = self.x + rightOperand.x
		obj.y = self.y + rightOperand.y
		return obj

	def __sub__(self, rightOperand):
		obj = A();
		obj.x = self.x - rightOperand.x
		obj.y = self.y - rightOperand.y
		return obj

a1 = A(10, 30)
a2 = A(20, 200)
a3 = a1 + a2
a4 = a1 - a2

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(a4.__dict__)
