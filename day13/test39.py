class A:
    def test1(self):
        self.test2()

    def test2(self):
        print('Hello')

a1 = A()
a1.test1()
