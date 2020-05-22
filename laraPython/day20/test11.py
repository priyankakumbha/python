
def my_generator():
	i = 0;
	while i <= 20:
		if i % 5 == 0:
			yield i
		i += 1
g1 = my_generator()
for e1 in g1 :
	print(e1, end=", ")

print();

list = [0, 5, 10, 15, 20];
for i in list:
	print(i, end=", ")