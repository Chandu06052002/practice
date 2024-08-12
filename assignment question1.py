 # to print the n integral number with theur square form in the dictionary form

input_dic = eval(input("enter your n value :"))
output_dic={}
for i in range(1,input_dic+1):
    key = str(i)
    value = int(i * i)
    output_dic[key] = value
print(output_dic)

# to print the comma seperated output in the form of list and tuple

input_values =input("enter the value :")


output_list = input_values.split(",")
output_tuple = tuple(output_list)

print(output_list)
print(output_tuple)

# to print sorted of words with comma seperated 

input_words = input("enter the input words :")
words  = input_words.split(",")
result_words = sorted(words)
result_words = ",".join(result_words)
print(result_words)

# to count the letters and digits given in the string and have to print the output

input_string = input("enter the string :")

numbers_count = 0
letters_count = 0

for char in input_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        numbers_count += 1

print(f"letters {letters_count},digits{numbers_count}")

# to count upper case and lower case letters in string

input_string = input("enter a string :")

uppercase_count = 0
lowercase_count = 0

for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    
print(f"uppercase letters {uppercase_count},lowercase letters {lowercase_count}")


# to check the password contains the required characters or not

input_password = input("enter the input password :").split(",")
valid_password =[]

for password in input_password:
    password = password.strip()
    if len(password) > 6 or len(password) < 12:
        continue

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$@#":
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        valid_password.append(password)

print(",".join(valid_password))



# to create a program on bank account like deposit and withdraw

input_amount = input("enter the amount :").split()

current_amount = 0

for i in range(0,len(input_amount),2):
    type = input_amount[i]
    amount = int(input_amount [i+ 1])

    if type == "D":
        current_amount += amount
    elif type == "w":
        current_amount -= amount

print(current_amount)

# to find the number that are divisible by 7 but not multiple of 5
# in the range of 2000 to 3200

result = []

for nums in range(2000,3200):
    if nums % 7 == 0 and nums % 5 != 0:
        result.append(str(nums))

print(",".join(result))


# to square value of the keys of the dictionary using function
result ={}
def square_values(key):
    for i in range(1,key+1):
        keys = str(i)
        values = int(i * i)
        result[keys] = values
    print(result)

square_values(10)


# to print square valus in the list for last 5 digits


def square_list():
    result_list=[i * i for i in range(1,20+1)]
        
    print(result_list[-5:])

square_list()
    


