def decorator(f1):
	def origianl_with_dec():
		print("before")
		f1()
		print("after")
	return origianl_with_dec;


@decorator
def original():
	print("from original")


original()
original()
original()
original()
original()





