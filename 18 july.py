# isalnum() operation in strings

word1 = "chandu1223"
print(word1.isalnum())

# isalpha() operation in strings

word2 = "chandu"
print(word2.isalpha())

# isdigit operation in strings

word3 = "1234567"
print(word3.isdigit())

# isupper operation in strings

word4 = "CHANDU"
print(word4.isupper())

# islower operation in strings

word5 = "chandu"
print(word5.islower())

# istitle operation in strings

word6 = "We Have Pleanty Of Knowledge"
print(word6.istitle())

# isspace operation in strings

word7 =" "
print(word7.isspace())

# to convert uppercase vowles into lowercase and vice versa

data  = "KNOWLEAGE IS SHARPER THAN THE KNIFE,knife is not sharper than knowlwdge"
vowles = "aeiouAEIOU"
converted_data = ""

for out in data:
    if out in vowles:
       if out.islower():
           converted_data += out.upper()
       else:
           converted_data += out.lower()
    else:
        converted_data += out
print(converted_data)





     