class A:
	def __init__(self, i) :
		self.i = i

class B(A):
	pass

b1 = B(10)
print(b1.__dict__)