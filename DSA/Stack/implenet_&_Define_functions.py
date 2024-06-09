#define stack  class , define methods -> pop, push, peek, is_empty, size

from collections import deque
class stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        return self.container.append(val)
    #pop function
    def pop(self):
        if self.is_empty():
            print("stack underflow")
        else:
            return self.container.pop()
    
    #peek function
    def peek(self):
        return self.container[-1]
    
    #is empty function
    def is_empty(self):
        return len(self.container)==0
    
    #size function
    def size(self):
        return len(self.container)


#create object of stack class
s = stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.push(25)

print(s.peek())
print(s.pop())
print(s.pop())

print(s.is_empty())
print(s.size())

