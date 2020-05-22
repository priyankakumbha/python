import sys

class A:
	pass


a1 = A()
print(sys.getrefcount(a1))
a2 = a1
print(sys.getrefcount(a1))
a3 = a2
print(sys.getrefcount(a1))
a4 = a3
print(sys.getrefcount(a1))
print("----")
del a1;
del a2;
print(sys.getrefcount(a4))
print("----")
del a3;
print(sys.getrefcount(a4))
del a4;
print(sys.getrefcount(a4))
#print(sys.getrefcount(self))





