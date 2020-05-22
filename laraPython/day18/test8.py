f1 = open("hello2.txt", 'r');
lines = f1.readlines();
for line in lines:
	print(line)
f1.close()