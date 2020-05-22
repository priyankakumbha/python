class A:
	pass

a1 = A();
a2 = A()

a1.i = 3000;
a2.j = 'abc'
a1.k = 'hello';
a2.m = 'hello';

a1.x = a2;

print(a1.i, a1.k, a1.x.j, a1.x.m)