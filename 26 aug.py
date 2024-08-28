# Encapsulation

# public attribute method

class Work:
    def __init__(self,value):
        self.value = value
    def num(self):
        print(self.value)
w =Work(478)
print(w.value)
w.num()

# protected attribute and method

class Work1:
    def __init__(self,num):
        self._num = num
    def details(self):
        print(self._num)
w = Work1("welcome")
print(w._num)
w.details()

#private attributes and method

class Work3:
    def __init__(self,num1):
        self.__num1 = num1
    def detail(self):
        print(self.__num1)
ww = Work3(6373)
ww.detail()



class Number1:
    def __init__(self,x):
        self.x = x
    def low(self):
        print(self.x)

class Number2:
    def __init__(self,y):
        self._y = y
    def low1(self):
        print(self._y)

class Number3:
    def __init__(self,z):
        self.__z = z
    def low2(self):
        print(self.__z)

n1 =Number1("Welcome")
n1.low()
print(n1.x)

n2 = Number2("This is project")
n2.low1()
print(n2._y)

n3=Number3("Encapsulation")
n3.low2()
#print(n3.__z)

