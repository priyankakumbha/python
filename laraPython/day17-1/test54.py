print(1)
try:
	print(2)
	i = int(input("enter int value:"));
	print(3)
	j = i / (i - 9)
	print(4)
except ValueError:
	print("I am from Value error")
except ZeroDivisionError:
	print("I am from ZeroDivisionError")
else:
	print(" i am from else block")
print(5)