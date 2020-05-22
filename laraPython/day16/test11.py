class A:
	def __init__(self):
		print("constructor is executing")

	def __del__(self):
		print("destructor is executing")


a1 = A()
a1 = None;
a2 = A()
a2 = None
a3 = A()
print("done")

