class A:
	def test(self):
		print("from A.test")

class B(A):
	def test(self):
		print("from B.test")

list = [A(), B()];

for obj in list:
	obj.test();


