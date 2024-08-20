#different types of methods in python

# class method

class Value:

    number = 50
    @classmethod
    def num(cls):
        print(cls.number)
    @classmethod
    def num1(cls,value):
        cls.number = value

Value.num()
result = Value()
result.num()
Value.num1(100)
Value.num()

# static method 

class Calculation:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def multiply(x,y):
        return x * y
    
    @staticmethod
    def avg(x,y):
        return (x+y)%2
    
addition = Calculation.add(5,5)
multiplication = Calculation.multiply(4,10)
average = Calculation.avg(5,9)

print(addition)
print(multiplication)
print(average)


# instance method

class Person:

    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def greet(self):
        return f'i am {self.name} and i am {self.age} years old'
    
    def address(self):
        self.address = "newyork"
        print(f'my self {self.name},and i am {self.age} i stay at {self.address}')

person = Person("chandu",22)
print(person.greet())
person.address()
print(person.greet())