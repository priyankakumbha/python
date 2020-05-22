print(1)
try:
	print(2)
	x = 20
	y = 10 / 0
	print(3)
except:
	print("except begin", x)
	print("except end")
print(4, x)
