#create a hash table in which we will be able to perform 
# opertaions:
# 1- Addition of an item in hash table
# 2- Extraction of any item in the hash table
# 3- Creation of any hash function


class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]
    
    def hash_function(self,key):
        summation = 0
        m = 10        
        for char in key:
            summation += ord(char) 
    
        return summation %m
    
    # addition of item in the hash table
    def addItem(self,key,value):
        h =  self.hash_function(key)
        self.arr[h] = value
        
    # extraction of item from hash table
    def getItem(self,key):
        h = self.hash_function(key)
        return self.arr[h]

# object created
obj = HashTable()
print(obj.arr)
obj.addItem("March 2020",234)
obj.addItem("March 2021",345)
obj.addItem("March 2022",445)
obj.addItem("March 2023",553)

print(obj.arr)

print(obj.getItem("March 2023"))
 