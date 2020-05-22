class A:
	obj_count = 0;
	def __init__(self):
		print("constructor is executing")
		A.obj_count += 1

	def __del__(self):
		print("destructor is executing")
		A.obj_count -= 1


a1 = A()
a2 = A()
a3 = A()
print("object count @ 1:", A.obj_count)
a1 = None;
print("object count @ 2:", A.obj_count)
a2 = None;
print("object count @ 3:", A.obj_count)
a3 = None;
print("object count @ 4:", A.obj_count)

