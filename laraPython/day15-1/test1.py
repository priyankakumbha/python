from abc import ABC, abstractmethod
class X:
	pass

class Y(ABC):
	pass

class Z:
	@abstractmethod
	def f1(self):
		print("some thing")
		

class P(ABC):
	@abstractmethod
	def f1():
		print("from P.f1")

ref1 = X()
ref2 = Y()
ref3 = Z()

ref4 = P()
print("done")

