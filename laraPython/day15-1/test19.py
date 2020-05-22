class A:
	def __init__(self, p1 = 0):
		self.x = p1;


	def __add__(self, rightOperand):
		obj = A();
		obj.x = self.x + rightOperand.x
		return obj

	def __sub__(self, rightOperand):
		obj = A();
		obj.x = self.x - rightOperand.x
		return obj

	def __gt__(self, rightOperand):
		return self.x > rightOperand.x;

a1 = A(10)
a2 = A(20)
a3 = a1 + a2
a4 = a1 - a2

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(a4.__dict__)
print(a1 > a2)
print(a1 > a3)
print(a1 > a4)
print(a2 > a4)
print(a3 > a4)
