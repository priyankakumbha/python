import functools

x = [1, 2, 5, 7, 4, 2];
print(x)

def test1(a, b):
    return a * b;

y = functools.reduce(test1, x)


print(y)
