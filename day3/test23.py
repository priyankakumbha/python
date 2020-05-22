def test(arg1):
    def case1():
        print('i am from case1')
        print('i am from case1')

    def case2():
        print('i am from case2')
        print('i am from case2')

    def case3():
        print('i am from case3')
        print('i am from case3')

    d1 = {
    1: case1,
    2: case2,
    3: case3,
    }
    # d1.get(arg1)()
    d1.get(arg1)()

test(2)
