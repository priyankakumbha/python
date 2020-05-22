x = [10, 200, 15, 35, 40, 200, 150, 40, 65];
print(x)

y = filter(lambda a : a % 5 == 0, x)
z = filter(lambda a : a % 10 == 0, x)

print('5's numbers', list(y))
print('10's numbers', list(z))
