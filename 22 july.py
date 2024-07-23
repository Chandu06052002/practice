# to add element at the end of array 

input = ["hello",1,15.23,True]
input.append("welcome")
print(input)

# to insert the element at given location

input = ["hello",63,66.32,True]
input.insert(1,26)
print(input)

# to check the sizes of 2 lists

lst1 = [10,20,30,40,90]
lst2 = [50,60,70,80]

if len(lst1) == len(lst2):
    print("the sizes of 2 lists are same")
else:
    print("the sizes of the lists are not same")

# to create a python list in all possible ways

# 1 declaring dirctly 
lst = ["fruits",100,28.4,True]
print(lst)

# 2 by using the split option

lst = "10,20,30,40,50"
result = lst.split()
print(result)

# to access the elements in the nested list

input_lst = [10,20,30,[40,50,60,[70,80,90]]]

result1 = input_lst[0]
result2 = input_lst[3]
result3 = input_lst[3][0]
result4 = input_lst[3][3]
result5 = input_lst[3][3][0]
result6 = input_lst[3][3][2]
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)

# to reverse a list in possible ways

# using slice we can reverse the list

input_lst = [10,20,30,40,50]
result = input_lst[::-1]
print(result)

# using reverse keyword 

input= ["apple","banana","pine apple","grapes"]
input.reverse()
print(input)

# sum of elements in the list

input_items = [10,20,30,40,50]
sum_of_items = 0

for total in input_items:
    sum_of_items += total
    
print(sum_of_items)

