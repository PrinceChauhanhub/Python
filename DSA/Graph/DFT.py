# Depth First Traversal 

def depth_first_traversal(visited,graph,node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for adjacent_node in graph[node]:
            depth_first_traversal(visited, graph, adjacent_node)

visited = set()

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

depth_first_traversal(visited , graph, '5')