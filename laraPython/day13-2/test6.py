class X:
	i = 100
	j = 'abc'
print(X.i)
print(X.j)
obj = X()
print(obj.i)
print(obj.j)
obj.i = 4000
obj.j = 700;
print(X.i)
print(X.j)
print(obj.i)
print(obj.j)
obj.i = 'hello'
obj.j = 4.5;
print(X.i)
print(X.j)
print(obj.i)
print(obj.j)
