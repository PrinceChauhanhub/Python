class HashTable:
  def __init__(self):
    ## size of hashtable is 10
    self.MAX = 10
    ## intialize all elements as None
    self.arr = [[] for i in range(self.MAX)]

  ## hash function method definition
  def hash_function(self, key):
    summation = 0
    for char in key:
      summation += ord(char)
    ## division modulo hash function
    return summation % self.MAX

  ## addition of an item in the hash table
  def __setitem__(self, key, value):
    found = False
    h  = self.hash_function(key)

    for index, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[0] == key:
        self.arr[h][index] = (key, value)
        found = True
        break

    if not found:
      self.arr[h].append((key, value))
  
  ## get any item from the hash table
  ## element - (key, value)
  ## element[0] - key
  ## element[1] - value
  def __getitem__(self, key):
    h = self.hash_function(key)
    for index, element in enumerate(self.arr[h]):
      if element[0] == key:
        return element[1]

  
  ## delete the item from the hashtable
  def __delitem__(self, key):
    h = self.hash_function(key)
    for index, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][index]
        
        
        
obj2 = HashTable()
obj2['march 6'] = 20
obj2['march 17'] = 27    
print(obj2.arr)
  
print(obj2["march 17"])

del obj2["march 6"]

print(obj2.arr)
 