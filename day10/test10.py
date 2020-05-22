import functools

x = [1, 20, 15, 35, 4, 2];
print(x)

def test1(a, b):
    return a + b;

y = functools.reduce(lambda a,b : a+b , x)


print(y)
