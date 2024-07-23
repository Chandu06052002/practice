# list operations
# declaring the list 

lst = ["hello",68239,646.737,True]
print(lst)
print(type(lst))

# taking lst values using index 

lst = [1,2,3,4,5,6,7,8,9,0]
lst1 = lst[4]
lst2 = lst[3]
lst3 = lst[2]
lst4 = lst[-1]
print(lst1,lst2,lst3,lst4)

# list inside a list 

lst =[1,2,3,[4,5,6]]
result1 = lst[3]
result2 = lst[3][0]
print(result1,result2)

# inserting value in list 

lst = [1,2,3,4,5,6]
lst.insert(3,9)
print(lst)

lst.insert(-1,66)
print(lst)

# appending values in the list

lst = ["apple","orange","banana","pineapple"]
lst.append("grapes")
print(lst)

lst.append("watermelon")
print(lst)