import threading 
x = 0
def increment(): 
	global x 
	x += 1
def thread_task(lock): 
	for _ in range(100000): 
		lock.acquire() 
		increment() 
		lock.release() 
for i in range(10):
	x = 0
	lock1 = threading.Lock() 
	#lock2 = threading.Lock() 
	t1 = threading.Thread(target=thread_task, args=(lock1,)) 
	t2 = threading.Thread(target=thread_task, args=(lock1,)) 
	t3 = threading.Thread(target=thread_task, args=(lock1,)) 
	t1.start() 
	t2.start() 
	t3.start() 
	t1.join() 
	t2.join() 
	t3.join() 
	print('iteration', i, x);