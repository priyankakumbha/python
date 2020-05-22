def test1():
	print(1)


def test2(arg):
	print(2);
	arg();
	print(3)

print(4)
test2(test1);
print(5)