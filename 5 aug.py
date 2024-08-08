# to print the value of random modules 

import random
import random

num1 = random.randint(1,10)
print(num1)

# to print strings using using random module

import random
word1 = ["python","java","django","html","css"]
result = random.choice(word1)
print(result)

# by using for loop to print random value 

for i in range(10):
    print(random.randint(1,10))

# math module

#square root
import math
num2 =math.sqrt(81)
print(num2)

num3 = math.pow(3,3)
print(num3)

num4 = math.factorial(6)
print(num4)

#ceil()

num5 = math.ceil(4.1)
print(num5)

# floor()

num6 = math.floor(5.5)
print(num6)

# date and time module
import datetime

from datetime import time

t = time(15,20,20)
print(t)

t1 = datetime.datetime.now()
print(t1)

today = datetime.date.today()
print(today)

# calender module

import calendar
cal = calendar.month(2024,9)
print(cal)

