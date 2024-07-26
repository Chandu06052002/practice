# program on to create a set

s = {10,20,30,"python","django",True,False,20.33,63.83}
print(type(s))
print(s)

# program on the iteration over sets

s1 = {5,10,15,20,25,30,35,40,45,50}

for items in s1:
    print(items)

# to add a memeber into the set

s2 = {"python","html","css"}
s2.add("django")
s2.add("js")
print(s2)

# to remove the member from the set 

s3 = {10,20,30,40,50,60}
s3.remove(30)
s3.remove(20)
print(s3)

# to create a intersection of sets

developing_team = {"gopi","venkat","ardash","jagan","namratha","swathi"}
support_team = {"mohammad","krishna","srivani","ardash","venkat","gopi"}
result = developing_team.intersection(support_team)
print(result)

# to create union of sets

aadhar_upgrade = {"ajay","venu","gopal","chandu","namratha","ardash"}
pancard_apply = {"venkat","gopi","namratha","jagan","vikram","virat","rahul"}
result2 = aadhar_upgrade.union(pancard_apply)
print(result2)

# to create the difference between sets

french_lang = {"vihar","villi","lucky","krish","vimal","vivek"}
dutch_lang = {"vimal","vivek","tharun","vishnu","mahesh","rohit"}
result3 = french_lang.difference(dutch_lang)
print(result3)

# to create the symmetric difference in sets
   
french_lang = {"vihar","villi","lucky","krish","vimal","vivek"}
dutch_lang = {"vimal","vivek","tharun","vishnu","mahesh","rohit"}
result4 = french_lang.symmetric_difference(dutch_lang)
print(result4)

# to find the max and min value of the sets

values = {10,20,30,40,50}
result5 = max(values)
result6 = min(values)
print(result5)
print(result6)

# to update the first that elements not present in second set

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

result7 = set1.difference(set2)
print(result7)

# to remove the given elements in set at once

elements = {10,20,30,40,50,60}
items_remove = {10,20,30}

for item in items_remove:
    elements.remove(item)
    print(elements)

# to display common elements in the 2 sets 

set1 ={10,20,30,40,50}
set2 ={30,40,50,60,70}
common_elements =set()

for items1 in set1:
    if items1 in set2:
        common_elements.add(items1)
print(common_elements)
   

# adding items set2 items to set1 without common elements

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

for items in set2:
        if items not in set1:
             set1.add(items)
print(set1)


# to take common elements in both sets

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

common_elements = {item for item in set1 if item in set2}

set1.clear()
set1.update(common_elements)
print(set1)