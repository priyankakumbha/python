class A:
	pass

class B(A):
	pass

class C(A):
	pass

class D(C):
	pass


a1 = A()
b1 = B()
c1 = C()
d1 = D()

print(isinstance(a1, A))
print(isinstance(a1, B))
print(isinstance(a1, C))
print(isinstance(a1, D))


print(isinstance(b1, A))
print(isinstance(b1, B))
print(isinstance(b1, C))
print(isinstance(b1, D))

print(isinstance(c1, A))
print(isinstance(c1, B))
print(isinstance(c1, C))
print(isinstance(c1, D))

print(isinstance(d1, A))
print(isinstance(d1, B))
print(isinstance(d1, C))
print(isinstance(d1, D))






