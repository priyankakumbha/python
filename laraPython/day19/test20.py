def f1(arg1, arg2):
	print("from f1", arg1, arg2)

def arg_func_decorator(func):
	def arg_func_origianl_with_decoration(x, y):
		print("begin", x, y)
		func(x, y)
		print("end", x, y)
	return arg_func_origianl_with_decoration;


f1('abc', 'xyz');
print("-----")
f2 = arg_func_decorator(f1)
f2('abc', 'xyz')


