#creating a tuple
colours=("red","green","blue")

#creating a tuple with single item
fruit=("apple",)
      #or
fruit=tuple("apple")

#type of tuple
print(type(fruit))

#length of tuple
print(len(colours))

#accessing item in tuple 
#1(positive indexing)
print(colours[1])

#2(negative indexing)
print(colours[-2])

#slicing a tuple
#1(positive indexing)
print(colours[1:3])

#2(negative indexing)
print(colours[:-2])

#item exist in tuple
if "blue" in colours:
    print("present")

#traverse a tuple
for i in colours:
    print(i)
    
#cocatenate a tuple
colours2=("green","brown")

colours=colours + colours2
print(colours)

#unpacking a tuple
names=("prince","shushma","pragati")
name1,name2,name3=names
print(name1,name2,name3)