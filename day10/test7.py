x = [10, 200, 15, 35, 40, 200, 150, 40, 65];
print(x)


def test1(a):
    return a * 3;

def test2(a):
    return a + 8;

y = map(test1, x)
z = map(test2, x)

print(list(y))
print(list(z))
