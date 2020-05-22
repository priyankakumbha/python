import functools

x = [1, 2, 5, 7, 4, 2];
print(x)

y = functools.reduce(lambda a, b : a * b, x)
print(y)
