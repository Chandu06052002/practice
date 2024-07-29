# to check the occurance of a character in a string

input_string = input("enter a string")
char_count = []
repeated_chars = []
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    if count > 1:
        repeated_chars.append(char)
print("Repeated characters:", repeated_chars)

# to check the 2 strings will be anagram or not

input_string1 = input("enter the string 1")
input_string2 = input("enter the string 2")

string1 = input_string1.replace(" ","").lower()
string2 = input_string2.replace(" ","").lower()

if len(string1) != len(string2):
    print("the string1 and string2 is not an anagram string")
else:
    if sorted(string1) == sorted(string2):
        print("the string 1 and string 2 is a anagram string")
    else:
        print("these are not anagram string")

# to check the given string or number is palindrome or not

input_string = input("enter a string")
rev = input_string[::-1]

if input_string == rev:
    print("it is palindrome ")
else:
    print("it is not palindroma")

# to replace the space in a string without using replace keyword

input_string = "welcome to python session"
new_char = "-"
modified_string = []
for char in input_string:
    if char == " ":
        modified_string.append(new_char)
    else:
        modified_string.append(char)

new_string = "".join(modified_string)
print(new_string)

# replace space with a given character

first_string = "this is the string"

result_string = first_string.replace(" ","123")
print(result_string)

# to convert lower cases to upper cases 

input_string = "this string is lower case"

result = input_string.upper()
print(result)

# to convert the upper case to lower case

input_string = "THIS STRING IS UPPER CASE STRING"

result = input_string.lower()
print(result)
