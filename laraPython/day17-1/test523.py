print(1)
def test():
	try:
		print(2)
		return 100;
	except ZeroDivisionError as msg:
		print(3, type(msg))
	finally:
		print("from finally")
	print(4)
print(5)
print(test())
print("end")