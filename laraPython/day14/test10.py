class A:
	def __init__(self, i) :
		self.i = i

class B(A):
	def f1(self, k):
		self.k  = k


b1 = B(10)
print(b1.__dict__)
b1.j = 20
print(b1.__dict__)
b1.f1(30)
print(b1.__dict__)