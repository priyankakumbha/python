class A:
	def test(self):
		print("from A.test")

class B(A):
	def test(self):
		print("from B.test")

class C(B):
	def test(self):
		print("from C.test")
class D(A):
	def test(self):
		print("from D.test")

list = [A(), B(), C(), D()];

for obj in list:
	obj.test();


