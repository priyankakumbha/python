'''
class A:
	class B:
		def test(self):
			print(1)
		class C:
			def f1(self):
				print(11)
a1 = A()
b1 = a1.B()
b1.test()
c1 = b1.C()
c1.f1()
c2 = A().B().C();
c2.f1()
'''
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()