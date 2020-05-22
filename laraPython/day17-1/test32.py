print(1)
try:
	print(2)
	i = 10 / 0
	print(3)
except (IndexError, ZeroDivisionError):
	print("from Error ")
print(4)
