try:
	f1 = open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Jellyfish.jpg', 'rb')
	f2 = open('hello4.jpg', 'wb')
	b1 = f1.read()
	f2.write(b1)
except BaseException as err:
	print(err)
finally:
	f1.close()
	f2.close()
