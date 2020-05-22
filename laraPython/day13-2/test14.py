class A:
	x = 100

a1 = A()
print(A.x)

A.y = 4000
A.z = 5000

print(A.x, A.y, A.z)
print(a1.x, a1.y, a1.z)