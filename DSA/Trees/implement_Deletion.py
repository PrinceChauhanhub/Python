# applying inorder sucessor
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
   
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

def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data) + " " ,end = " ")
        inOrder(root.right)  
  
def minNode(root):
    present = root
    while present.left:
        present = present.left
    return present

def deleteNode(root,ele):
    if root is None:
        return root
     
    if root.data < ele:
         root.right = deleteNode(root.right,ele)
    if root.data > ele:
        root.left = deleteNode(root.left,ele)
    else:
        # if there is only one child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        #find the minimum in right subtree, which is the successor of present rootnode
        tempnode = minNode(root.right)
        root.data = tempnode.data 
        root.right = deleteNode(root.right,tempnode.data) 

    return root

root = Node(50)
root = insertBST(root,40)
root = insertBST(root,70)
root = insertBST(root,60)
root = insertBST(root,80)

inOrder(root)
print()
deleteNode(root,80)
inOrder(root)  