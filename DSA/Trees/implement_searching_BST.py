class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # Insertion of node
def insertBST(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif(root.data < key):
            root.right = insertBST(root.right,key)
        else:
            root.left = insertBST(root.left,key)
    return root

def searchBST(root, key):
    if root is None or root.data == key:
        return root
    if root.data > key:
        return searchBST(root.left,key)

    return searchBST(root.right,key)

root = Node(50)
root = insertBST(root,40)
root = insertBST(root,70)
root = insertBST(root,60)
root = insertBST(root,80)

if (searchBST(root,40)):
    print("element is in the BST")
else:
    print("element is not in the BST")