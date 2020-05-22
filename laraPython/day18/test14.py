try:
	f1 = open('D:\\JDK8.0\\test1.txt', 'a')
	f1.write('abc')
	f1.write('abc')
	f1.write('abc')
except BaseException as ex:
	print(ex)
finally:
	f1.close()

print("done");