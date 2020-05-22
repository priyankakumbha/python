import threading

def test1():
	print('I am from test:', threading.current_thread().name)

print('from main stack', threading.current_thread().name)

t1 = threading.Thread(target=test1)
t1.start()
#t1.run()

