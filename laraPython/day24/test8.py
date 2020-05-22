import threading

def test1():
	for i in range(50):
		print(i, threading.current_thread().name)


t1 = threading.Thread(target=test1)
t1.start()

t1.join();


print('from main stack', threading.current_thread().name)

