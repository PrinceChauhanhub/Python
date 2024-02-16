fruits = ["apple","mango","cherry","banana"]

print(fruits)

print(type(fruits))
#lenght of list
print(len(fruits))
#check element is present or not using 'in' keyword
if "banana" in fruits:
    print("Banana is present")

if "kiwi" not in fruits:
    print("kiwi is not present")
    
#indexing in list
print(fruits[1])    

print(fruits[-3])    

print(fruits[1:3])    

print(fruits[-3:-1])    