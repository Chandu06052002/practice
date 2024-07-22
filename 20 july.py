# to seperate the characters of a given string

input_string = "new program in python"
seperate_string = []

for char in input_string:
    seperate_string.append(char)
    seperate_string.append(" ")

new_string = "".join(seperate_string)
print(new_string)

# to remove blank spaces from the string

input_string = "h e l l o w o r l d"

seperate_string = ""
for char in input_string:
    if char != " ":
        seperate_string += char
print(seperate_string)

# to concate 2 string usin join() operation 
 
input_string1 = "hello"
input_string2 = "world"

result = " ".join([input_string1,input_string2])
print(result)

# concentation of 2 strings without usng join() operation

input_string1 = "hello"
input_string2 = "world"
print(input_string1+" "+input_string2)

