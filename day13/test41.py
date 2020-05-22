class A:
    def __init__(self):
        print('first constrctor')

    def __init__(self,i):
        print('second constrctor')

    def __init__(self,i,j):
        print('third constrctor')

# a1 = A()
# a2 = A(10)
a2 = A(10,20)
