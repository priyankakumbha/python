class AgeNegativeError(ValueError):
	def __init__(self, param):
		self.msg = param
		ValueError.__init__(self, param)


print(1)
try:
	print(2)
	i = int(input("enter age:"))
	if i <= 0:
		raise AgeNegativeError('age should not be negative')
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")
	print("continue ...")

except AgeNegativeError as err:
	print("from except", err)
print("end")

