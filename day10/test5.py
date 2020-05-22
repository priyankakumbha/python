x = [10, 200, 15, 35, 40, 200, 150, 40, 65];
print(x)

y = filter(lambda a : a % 2 == 0, x)
z = filter(lambda a : a % 2 == 1, x)

print('even numbers', list(y))
print('odd numbers', list(z))
