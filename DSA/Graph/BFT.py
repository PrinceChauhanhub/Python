# Breadth first traversal
from collections import deque
queue = deque()
def breadth_first_traversal(graph,visted,node):
    visted.add(node)
    
    queue.appendleft(node)
    
    while queue:
        node = queue.pop()
        print(node,end = " ")
         
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.appendleft(adjacent_node)
    
# driver code

graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['E','F'],
    'D':['F'],
    'E':['G'],
    'F':['G'],
    'G':[]
} 

visited = set()

breadth_first_traversal(graph,visited,'A')