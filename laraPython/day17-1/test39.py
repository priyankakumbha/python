print(1)

try:
	print(2)
	i = 10 / 0
	print("try end")
except ArithmeticError:
	print(3)
except ZeroDivisionError:
	print(4)
print(5)
