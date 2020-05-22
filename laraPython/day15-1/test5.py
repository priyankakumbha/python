from abc import ABC, abstractmethod

class P(ABC):
	@abstractmethod
	def f1(self):
		pass

	@abstractmethod
	def f2(self):
		pass

	def f3(self):
		print("P.f3")


class Q(P):
	def f4(self):
		print("P.f4")

class R(P):
	def f1(self):
		print("R.f1()")
	def f5(self):
		print("P.f5")

class S(P):
	def f2(self):
		print("S.f2()")
	def f6(self):
		print("S.f6()")


class T(S):
	def f1(self):
		print("T.f1()")
	def f7(self):
		print("T.f7()")



#ref1 = P()
#ref2 = Q()
#ref3 = R()
#ref4 = S()
ref5 = T()
ref5.f1()
ref5.f2()
ref5.f3()
ref5.f6()
ref5.f7()
print("done")

