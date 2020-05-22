def outer_func():
	print(1)
	print(2)
	def inner_func():
		print(3)
	print(4)
	inner_func()
	print(5)

print(6)
outer_func();
print(7)