print(1)
try:
	print(2)
	i = int(input("enter int value:"));
	print(3)
except ValueError:
	print("I am from Value error")
else:
	print(" i am from else block")
print(4)