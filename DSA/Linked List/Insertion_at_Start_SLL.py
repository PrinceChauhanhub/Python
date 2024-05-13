class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None

class LinkedList:
    def __init__(self):
        self.head=None

    ## Insert the node at Beginning of the Linked List
    def inserAtbeginning(self, new_data):
        # Create a new Node from the new data
        new_node = Node(new_data)

        # Insertion at beginning of LL
        new_node.nextPtr = self.head
        self.head = new_node
    
    # print the LL   
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.nextPtr
             
# Main Code
llist = LinkedList()
llist.inserAtbeginning(10)
llist.inserAtbeginning(20)
llist.inserAtbeginning(30)
llist.inserAtbeginning(40)
llist.inserAtbeginning(50)
  
llist.printLinkedList()
