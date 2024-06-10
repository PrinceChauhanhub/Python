from collections import deque
class Queue:
    def __init__(self):
        self.container = deque()
    
    def enqueue(self,val):
        return self.container.append(val)
    
    def dequeue(self):
        return self.container.popleft()

    def is_empty(self):
        return len(self.container)==0        
    
    def size(self):
        return len(self.container)
    def printQueue(self):
        print(self.container)
        
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.printQueue()

print(q.dequeue())
print(q.dequeue())

print(q.is_empty())

print(q.size())

     