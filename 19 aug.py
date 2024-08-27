# using super()
 
class Person:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
       
class Data(Person):
    def __init__(self,name,id,age,domain,salary):
        super().__init__(name,id,age)
        self.domain = domain
        self.salary = salary
       
 
d = Data("Chandu",81,22,"Python Developer",26000)
print(d.name)
print(d.id)
print(d.age)
print(d.domain)
print(d.salary)
 
# --------------------------------

class Car:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price
    def details(self):
        print(self.company)
        print(self.model)
        print(self.price)

class Vechile(Car):
    def __init__(self,company,model,price):
        super().__init__(company,model,price)
    
    def details(self):
        super().details()

c = Vechile("Mahindra","Thar",150000)
c.details()

# ------------------------------------

class Num:
    word1 = "welcome"
    def __init__(self):
        self.word2 = "Thank You"
class Word(Num):
    def max(self):
        print(self.word2)
        print(super().word1)

n = Word()
n.max()