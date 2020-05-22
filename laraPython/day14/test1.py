
class A:
	def __init__(self, i, j):
		self.i = i
		self.j = j


class B(A):
	pass

a1 = A(10, 20)
print(a1.__dict__)

b1 = B(100, 200)
print(b1.__dict__)