class AgeNegativeError(ValueError):
	def __init__(self, param):
		self.msg = param

	def __str__(self):
		return 'the reason for termination:' + self.msg

print(1)
try:
	print(2)
	i = int(input("enter age:"))
	if i <= 0:
		raise AgeNegativeError('age is negative')
	print("continue ...")
except AgeNegativeError as err:
	print("from except: ", err)
print("end")