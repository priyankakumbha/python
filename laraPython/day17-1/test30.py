print(1)
try:
	print(2)
	list = [100, 200]
	i = list[3]
	print(3)
except IndexError:
	print("from IndexError ")
print(4)
