def my_generator():
	print('stage1')
	yield 1
	print('stage2')
	yield 10
	print('stage3')
	yield 'abc'
g1 = my_generator()
for e1 in g1 :
	print("iteration begin")
	print(e1)
	print("iteration end")