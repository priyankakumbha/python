from abc import ABC, abstractmethod

class P(ABC):
	@abstractmethod
	def f1(self):
		pass

	@abstractmethod
	def f2(self):
		pass

class Q(P):
	pass

class R(P):
	def f1(self):
		print("R.f1()")

class S(P):
	def f2(self):
		print("S.f2()")


class T(S):
	def f1(self):
		print("T.f1()")



#ref1 = P()
#ref2 = Q()
#ref3 = R()
#ref4 = S()
ref5 = T()
res5.f1()
res5.f2()
print("done")

