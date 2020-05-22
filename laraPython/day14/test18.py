class A:
	def f1(self):
		print("A:f1()")
	def f2(self):
		print("A:f2()")

class B(A):
	def f1(self):
		print("B:f1()")

b1 = B()
b1.f1()
b1.f2()

