#creating dictionary
numbers={"jhon":8826970,"ria":7895331,"pragati":424542}
print  (numbers)

#type of dictionary
print(type(numbers))

#length of dictionary
print(len(numbers))

#access item of a dictionary
print(numbers["pragati"])
        #or
print(numbers.get("pragati"))

#print all keys
print(numbers.keys())

#print all the values
print(numbers.values())

#update value in dictionary
numbers["pragati"]=755653
print(numbers)

#add another element
numbers["prince"]=798577
print(numbers)

#add another dictionary
more_num={"rahul":23273}
numbers.update(more_num)
print(numbers)

#remove elements in dictionary
numbers.pop("rahul")
print(numbers)

#print keys of a dictionary
for x in numbers:
    print(x)
    
#print values of a dictionar
for x in numbers:
    print(numbers[x])

#print both keys and values
for x,y in numbers.items():
    print(x,y)

#empty the dictionary
numbers.clear()
print(numbers)

#nested dictionary
phones={
    "area1":{"x":0,"y":1,"z":2},
    "area2":{"a":3,"b":4,"c":5}
}

#access nested item  
print(phones["area1"]["z"])