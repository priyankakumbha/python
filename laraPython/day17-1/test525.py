print(1)
def test():
	try:
		print(2)
		print(3)
		return 200
	except ZeroDivisionError as msg:
		print(4, type(msg))
	finally:
		print("from finally")
		return 300
	print(5)
	return 500
print(6)
print(test())
print("end")