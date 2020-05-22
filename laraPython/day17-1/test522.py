try:
	print(1)
	x = 10 / 0
	print(2)
except ZeroDivisionError as msg:
	print(3, type(msg))
	i = 10 / 0
finally:
	print("from finally")
print(4)