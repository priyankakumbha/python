print(1)
try:
	print(2)
	i = int(input("enter age"))
	if i <= 0:
		raise ValueError("age should not be 0 or negative")
	print("continue ...")
except ValueError as msg:
	print("from except", msg)
print("end")