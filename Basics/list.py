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
        
#indexing in list add 
print(fruits[1])    

print(fruits[-3])    

print(fruits[1:3])    

print(fruits[-3:-1])    

#adding elements to a list 

list =[10,20,30,40]

##append method
list.append(50)
print(list)

#insert method
list.insert(2,25)
print(list)

list2=[70,80]

#extend method
list.extend(list2)
print(list)


#removing elements from a list
#pop method
list.pop(2)
print(list)

#remove method
list.remove(80)
print(list)

#change item in a list
#at a index

list[1]=15
print(list)

#in a range
list[1:3]=[25,35]
print(list)

