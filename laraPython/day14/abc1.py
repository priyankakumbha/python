class OverloadDemo:
    # sum method with one default parameter
    def sum(self, a, b, c=0):
            s = a + b + c
            return s

od =  OverloadDemo()
#calling method with 2 args
sum = od.sum(7, 8)
print('sum is-', sum)
#calling method with 3 args
sum = od.sum(7, 8, 9)
print('sum is-', sum)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayData(self):
        print('In parent class displayData method')
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        # calling constructor of super class
        super().__init__(name, age)
        self.empId = id

    def displayData(self):
        print('In child class displayData method')
        print(self.name)
        print(self.age)
        print(self.empId)

#Person class object
person = Person('John', 40)
person.displayData()
#Employee class object
emp = Employee('John', 40, 'E005')
emp.displayData()




#using + operator with integers to add them
print(5 + 7)
#using + operator with Strings to concatenate them
print('hello ' + 'world')
a = [1, 2, 3]
b = [4, 5, 6]
# using + operator with List to concatenate them
print(a + b)



For all operators internally Python defines methods to provide functionality for those operators. 
For example functionality for ‘+’ operator is provide by special method __add__(). 
Whenever ‘+’ operator is used internally __add__() method is invoked to do the operation.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #overriding magic method
    def __add__(self, other):
        return self.x + other.x, self.y + other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1+p2)


https://docs.python.org/2/library/operator.html