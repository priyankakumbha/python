from abc import ABC, abstractmethod

class A(ABC):
	pass

class B(A):
	pass

class C(B):
	pass


c1 = C()
print(isinstance(c1, ABC))
print(isinstance(c1, A))
print(isinstance(c1, B))
print(isinstance(c1, C))