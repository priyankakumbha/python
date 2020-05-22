print(1)
try:
	print(2)
	print(i);
	print(3)
except (NameError) as obj:
	print("except ", obj)
print(4)
