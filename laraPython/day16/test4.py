class A:
	pass

x = 10;
y = 10;
z = 10
a1 = A()
a2 = a1
a3 = a2
a4 = a3

print(id(x))
print(id(y))
print(id(z))
print(id(a1))
print(id(a2))
print(id(a3))
print(id(a4))