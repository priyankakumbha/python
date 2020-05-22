class Address:
    def __init__(self):
        self.house_no = None
        self.street_name = None
class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.address = None
p1 = Person()
p1.first_name = 'Shiva'
p1.last_name = 'Kumbhar'
p1.address = Address()
p1.address.house_no ='4/63'
p1.address.street_name = 'Tinderry CCT'
print(p1.__dict__,p1.address.__dict__)
