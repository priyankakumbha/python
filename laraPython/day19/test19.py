def f1(arg):
	print("from f1", arg)

def arg_func_decorator(func):
	def arg_func_origianl_with_decoration(x):
		print("begin", x)
		func(x)
		print("end", x)
	return arg_func_origianl_with_decoration;


f1('abc');
print("-----")
f2 = arg_func_decorator(f1)
f2('abc')


