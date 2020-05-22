i = input("enter a number:");
print(1)
try:
	print(2)
	j = int(i)
	print(3)
	k =  j / (j - 9)
	print(4)
	list = [10, 20, 30, 40, 50];
	m = list[j];
	print(5);
except ValueError:
	print("from ValueError ")
finally:
	print("i am from finally")
print(5)
