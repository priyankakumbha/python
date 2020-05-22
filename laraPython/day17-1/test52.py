import os

try:
	print(1)
	#os._exit()
	os._exit(1)
	print(2)
except BaseException as msg:
	print(3, type(msg))
finally:
	print("from finally")
print(4)