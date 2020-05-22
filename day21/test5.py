class A:
	class B:
		def f1(self):
			print("from B.f1")
	def f2(self):
		print("from A.f2")

	class C:
		def f3(self):
			print("from C.f3")
a1 = A()
a1.f2()


b1 = A().B()
b1.f1()

c2 = A().C()
c2.f3();
