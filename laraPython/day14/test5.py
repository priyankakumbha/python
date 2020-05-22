
class A:
	def __init__(self, i, j):
		self.i = i
		self.j = j


class B(A):
	def __init__(self, i, j, k):
		#super().__init__(i, j);
		#self.i = i
		#self.j = j
		obj = A(i, j)
		print(obj.i, obj.j);
		self.k = k;


a1 = A(10, 20)
print(a1.__dict__)

b1 = B(100, 200, 300)
print(b1.__dict__)