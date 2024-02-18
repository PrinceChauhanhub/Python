#creating a set
names={"sia","mia","tia"}

print(names)

#length of set
print(len(names))

#check data type of set
print(type(names))

#accesing item of a set
for i in names:
    print(i)
    
#check element exist or not
if "sia" in names:
    print("present")

#add elements in set
names.add("prince")
print(names)

#add another sequence in a set
names_list=["ria","pragati"]
names.update(names_list)
print(names)

#removing element from set 
names.remove("ria") #throw error if value not present
print(names)

     #or
names.discard("ta") #this function will not throw an error if value is not present in set
print(names)

#join 2 sets

s1={'a','b','c'}
s2={'d','e','a'}
print(s1,s2)

s3=s1.union(s2)
print(s3)
       #or
s1.update(s2)
print(s1)

#keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

#keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1) 

