# Node created
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

# PreOrder Traversal
def preOrder(root):
    if root:
        print(str(root.data) + " ",end = "  ")
        # left subtree
        preOrder(root.left)
        # Right subtree
        preOrder(root.right)

# InOrder Traversal
def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data)+" ",end = "  ")
        inOrder(root.right)
        
# postOrder Traversal
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.data)+" ",end ="   ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)