class A:
	i = 20;
	j = 'abc'
	
	def f1():
		print('from A.f1()')

	def f2():
		print('from A.f2()')


print(A.i)
print(A.j)
A.f1()
A.f2()

A.i = 500
A.j = 1500

print(A.i)
print(A.j)




