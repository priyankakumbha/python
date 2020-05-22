print(1)
try:
	print(2)
	print(i);
	print(3)
except NameError as obj:
	print("except begin", obj, obj.__class__, obj.__class__.__name__, type(obj))
print(4)
