print(1)
try:
	print(2)
	print(i);
	print(3)
except NameError as msg:
	print("except begin", msg)
	print("except end")
print(4)
