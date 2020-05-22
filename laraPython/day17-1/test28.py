print(1)
try:
	print(2)
	i  = 10 / 0
	print(3)
except ZeroDivisionError:
	print("from ZeroDivisionError ")
print(4)
