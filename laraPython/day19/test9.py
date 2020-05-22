def outer_func():
	print(2);
	def inner_func():
		print(3)
		return 200
	print(4)
	return inner_func;

print(5)
x = outer_func()
print(x)
print(6)