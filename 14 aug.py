# inheritence  and its types 

# single inheritance 

class Animal:
    def speek(self):
        return "animal sound"
    
class Dog(Animal):
    def speek(self):
        return "Bark"
    
dog = Dog()
print(dog.speek())

# multiple inheritance 

class Fly:
    def flying(self):
        return "fly very high"
    
class Hunting:
    def hunt(self):
        return "hunt fish"
    
class Eagle(Fly,Hunting):
    def speek(self):
        return "eeee"
    
bird = Eagle()
print(bird.speek())
print(bird.hunt())
print(bird.flying())


# multilevel inheritance 

class Animal:
    def eat(self):
        return "eating"
    
class Mammal(Animal):
    def breath(self):
        return "breathing air"

class Dog(Mammal):
    def speek(self):
        return "Bark"

d = Dog()
print(d.eat())
print(d.breath())
print(d.speek())    

# Hierarchical Inheritance

class Vechial:
    def travel(self):
        return "it contains engine and we can travel fastly"
    
class Car(Vechial):
    def drive(self):
        return "it is a four wheeler"
    
class Bike(Vechial):
    def ride(self):
        return "it is a two wheeler"
    
car = Car()
bike = Bike()

print(car.travel())
print(car.drive())
print(bike.travel())
print(bike.ride())

# hybrid inhetance

class Grandparent():
    def gp(self):
        return "reading"

class Parent1(Grandparent):
    def p1(self):
        return "writing"
    
class Parent2(Grandparent):
    def p2(self):
        return "gaming"
    
class Child(Parent1 , Parent2):
    def skills(self):
        return "all the skills"
    
child = Child()
print(child.gp())
print(child.p1())
print(child.p2())
print(child.skills())