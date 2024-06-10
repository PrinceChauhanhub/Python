## Print the binary numbers from 1 to 10

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
    def front(self):
        return self.container[0]

def produceBinaryNumber(n):
    q = Queue()
    q.enqueue("1")
    
    for i in range(n):
        front = q.front()
        print(front,end = " ")
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        
        q.dequeue()

n = 10
produceBinaryNumber(n)