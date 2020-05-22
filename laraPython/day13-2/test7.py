class Test:
	i  =100;
	j = 'abc'


print(Test.i)
print(Test.j)

t1 = Test();

print(t1.i)
print(t1.j)

Test.i = 5000;
Test.j = 'xyz';

print(t1.i)
print(t1.j)

