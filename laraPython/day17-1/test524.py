print(1)
def test():
	try:
		print(2)
		i = 10 / 0;
		print(3)
	except ZeroDivisionError as msg:
		print(4, type(msg))
		return 200
	finally:
		print("from finally")
	print(5)
print(6)
print(test())
print("end")