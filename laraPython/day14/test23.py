class A:
	def __init__(self):
		print("__init__()")
	def __init__(self, i):
		print("__init__(i)")

	def __init__(self, i, j , k):
		print("__init__(i, j)")

	def __init__(self, i, j):
		print("__init__(i, j)")

a1 = A(20, 4000)

print("done")
