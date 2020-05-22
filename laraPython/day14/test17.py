class A:
	def f1(self):
		print("from f1()")

	def f1(self, i):
		print("from f1(i)")

	def f1(self, i, j):
		print("from f1(i, j)")

	

a1 = A()
a1.f1(1, 2)
a1.f1(20, 3)
a1.f1(90, 8)
print("done")