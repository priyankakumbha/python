def log_decorator(func):
	def origianl_with_decorator():
		print("before executing", func.__name__)
		func()
		print("after executing", func.__name__)
	return origianl_with_decorator;

@log_decorator
def some_tx():
	print("from original")

some_tx();
print("--------")
some_tx()












