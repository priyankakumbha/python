try:
	f1 = open('D:\\JDK8.0\\test1.txt', 'r')
	print(f1.read())
except BaseException as ex:
	print(ex)
finally:
	f1.close()

print("done");