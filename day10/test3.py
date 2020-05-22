x = [10, 200, 15, 35, 40, 200, 150, 40, 65];
print(x)

def isEven(a):
    return a % 2 == 0

def isOdd(a):
    return a % 2 == 1


y = filter(isEven, x)
z = filter(isOdd, x)

print('even numbers', list(y))
print('odd numbers', list(z))
