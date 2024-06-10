from collections import deque
queue = deque()
queue1 = deque()

## Approach 1
queue.appendleft(5)
queue.appendleft(15)
queue.appendleft(25)

print(queue)

print(queue.pop())
print(queue.pop())


## Approach 2

queue1.append(12)
queue1.append(22)
queue1.append(32)

print(queue1)
print(queue1.popleft())
print(queue1.popleft())
 

