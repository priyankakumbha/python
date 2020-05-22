class A:
	def __init__(self):
		print("__init__()")
	def __init__(self, i):
		print("__init__(i)")
	def __init__(self, i, j):
		print("__init__(i, j)")

a1 = A()

print("done")