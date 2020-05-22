from abc import ABC, abstractmethod

class P(ABC):
	@abstractmethod
	def f1(self):
		print("P.f1")

class Q(P):
	pass

class R(P):
	def f1(self):
		print("R.f1()")

#ref1 = P()
#ref2 = Q()
ref3 = R()
#ref2.f1()
ref3.f1()
print("done")

