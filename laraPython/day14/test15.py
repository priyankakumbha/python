class A:
	def f1(self):
		print("from f1()")

	def f1(self, i):
		print("from f1(i)")

	

a1 = A()
a1.f1(20)
a1.f1(90)
print("done")