x = (12, 45, "abc", 45, "hello", 70.7878, 354, 12, 45, 'abc', 'abc' )
print(x)
y= list(x);
y[2] = 3000;
x = tuple(y)
print(x)
