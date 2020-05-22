print(1)
try:
	print(2)
	i = 10 / 0
	print(3)
except:
	print("except begin")
	i = 20 / 0
	print("except end")

print(4)
