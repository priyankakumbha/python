class Test:
    i = 100;
    j = 'abc'

print(Test.i)
print(Test.j)

t1 = Test();
t2 = Test();
t3 = Test();

print(t1.i, t1.j)
print(t2.i, t2.j)
print(t3.i, t3.j)

Test.i = 5000;
Test.j = 'xyz';

t1.i = 10
t1.j = 20

print(t1.i, t1.j)
print(t2.i, t2.j)
print(t3.i, t3.j)
