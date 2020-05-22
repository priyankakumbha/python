print(1)
try:
	print(2)
	i = 10
	if i <= 10:
		raise ValueError("some thing went wrong")
	print(3)
except ValueError:
	print("from except")
print(4)