class A:
    def __init__(self, data):
        self.data = data
        self.next = None

a1 = A(10)
a2 = A(20)
a3 = A(30)
a4 = A(40)
a5 = A(50)
a1.next = a2;
a2.next = a3;
a3.next = a4;
a4.next = a5;
a2 = a3 = a4 = a5 = None

element = a1;
while(element != None):
    print(element.data)
    element = element.next;
