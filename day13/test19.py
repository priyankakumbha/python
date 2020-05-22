class A:
    i = 10
    def test1():
        print('from test1')


a1 = A()
a2 = A()
a3 = A()

print(a1.i)
print(a2.i)
print(a3.i)

a1.test1()
a2.test1()
a3.test1()
