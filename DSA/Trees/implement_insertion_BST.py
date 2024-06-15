class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # Insertion of node
def insertBST(root,key):
    if root:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif(root.data < key):
            root.right = insertBST(root.right,key)
        else:
            root.left = insertBST(root.left,key)
    return root
def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data)+ " " ,end = " ")
        inOrder(root.right)        

root = Node(50)
root = insertBST(root,40)
root = insertBST(root,70)
root = insertBST(root,60)
root = insertBST(root,80)

print("Inoder traversal of the Tree :")
inOrder(root)
print()
    