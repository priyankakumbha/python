print(1)
try:
	print(2)
	print(i);
	print(3)
except NameError as err:
	print("except begin", err)
	print("except begin", err.__class__)
	print("except begin", err.__class__.__name__)
	print("except begin", type(err))
	print("except end")
print(4)
