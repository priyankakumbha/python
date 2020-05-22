def outer_func():
	print(2);
	def inner_func():
		print(3)
		return 200
	print(4)
	return inner_func();

print(5)
outer_func()
print(6)