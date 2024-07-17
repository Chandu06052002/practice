# find operation in string

name = "learning  python is very easy and it is coding easy"
print(name.find("very"))
print(name.rfind("easy"))

# index operation in string

name2 = "goood to learn python and it is very intersting to"
print(name2.index("learn"))
print(name2.rindex("to"))

# count operation in string

string = "Django can be (and has been) used to build almost any type of website — from content management systems and wikis, through to social networks and news sites. It can work with any client-side framework, and can deliver content in almost any format (including HTML, RSS feeds, JSON, and XML)."
print(string.count("a"))
print(string.count("b"))
print(string.count("c"))
print(string.count("d"))

# replace operaton in string

change = string.replace("and","123456")
print(change)

# spilt operation in string
 
num = "10,20,30,40,50"

result = num.split(",")
print(result)

#join operation in string

result1 = ".".join(result)
print(result1)

# uppercase operation of a string

word1 = "hii my self chandu"
print(word1.upper())

# lowercase operation of a string

word2 = "IT'S NICE TO MEET U"
print(word2.lower())

#swapping operation of string

word3 ="WHAT IS THE purpose of your prsence here"
print(word3.swapcase())

# title operation of string 

word4 = "introdyction to python"
print(word4.title())

# captalize operation in string

word5 = "learning is the greatest wealth"
print(word5.capitalize()) 

# startswith operation in string

word6 = "+91 5785567688"
print(word6.startswith("+91"))

# endswith operation in string 

word7 = "abcd@gmail.com"
print(word7.endswith(".com"))
