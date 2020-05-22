print(1)

try:
	print(2)
	i = 10 / 0
	print("try end")
except ZeroDivisionError:
	print(4)
except ArithmeticError:
	print(3)

print(5)
