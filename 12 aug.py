# to declare various types of variables in oops cocepts

# instaneous variable

class Actor:
    def __init__(self,name,number,value):
        self.name = name
        self.number = number
        self.value = value
    def action(self):
        print(self.name)
        print(self.number)
        print(self.value)
a=Actor('Adarsh',329,98)
a.action()
a.system = "intel"
print(a.system)


# static variable

class Numbers:
    nums = 30
    def __init__(self,value):
        self.value = value

    def num1(self):
        print(self.value)

    @classmethod
    def num2(cls):
        print(cls.nums)

print(Numbers.nums)
Numbers.value = 33
result = Numbers("value")
print(result.nums)
Numbers.num2()
print(result.nums)

# local variable

class Num:
    def  __init__(self,value):
        self.value = value

    def num1(self):
        value1 = 50
        print(value1)
        print(self.value)
result = Num("value")
result.num1()

