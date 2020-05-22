class A:
	class B:
		def f1(self):
			print("from B.f1")
		class C:
			def f3(self):
				print("from C.f3")
	def f2(self):
		print("from A.f2")

a1 = A()
a1.f2()

b1 = A().B()
b1.f1()

c1 = b1.C()
c1.f3();

c2 = A().B().C()
c2.f3();