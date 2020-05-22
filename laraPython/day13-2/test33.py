class A:
	def __init__(self, i, j):
		self.i = i;
		self.j = j;

	def print_data(self):
		print(self.i, self.j)


a1 = A(10, 20);
a2 = A(30, 40);
a3 = A('abc', 'hello')


a1.print_data()
a2.print_data()
a3.print_data()


