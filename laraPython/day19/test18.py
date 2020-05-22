def log_decorator(func):
	def origianl_with_log_decorator():
		print("before executing", func.__name__)
		func()
		print("after executing", func.__name__)
	return origianl_with_log_decorator;


def tx_decorator(func):
	def origianl_with_tx_decorator():
		print("tx starting", func.__name__)
		func()
		print("tx ending", func.__name__)
	return origianl_with_tx_decorator;


def some_functionality():
	print("from original")

some_functionality()
print("------")

f1 = log_decorator(some_functionality);
f1();
print("------")

f2 = tx_decorator(some_functionality);
f2();
print("------")
f3 = tx_decorator(f1)
f3()
