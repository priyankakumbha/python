print(1)
try:
	print(2)
	i  = 10 / 0
	print(3)
except NameError:
	print("except ")
print(4)
