# Time Complexity -> O(n)

class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None

class LinkedList:
    def __init__(self):
        self.head=None

    ## Insert the node at end of the Linked List
    def insertAtend(self,new_data):
        # Create a new Node from the new data
        new_node = Node(new_data)

        #check that linked list is not empty 
        if self.head is None:
            self.head = new_node
            return 
        
        # insert the data at the end
        temp = self.head
        while temp.nextPtr:
            temp=temp.nextPtr
        temp.nextPtr = new_node
    # Delete the node at any given position
    def deleteNode(self,position):
        if self.head is None:
            return
        temp=self.head
        for i in range(position-1):
            temp=temp.nextPtr
            if temp is None:
                return
        tempPtr=temp.nextPtr.nextPtr
        temp.nextPtr.nextPtr=None
        temp.nextPtr=tempPtr
        
    # print the LL
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.nextPtr
             
# Main Code
llist = LinkedList()
# Insertion of node at end of LL
llist.insertAtend(10)
llist.insertAtend(20)
llist.insertAtend(30)
llist.insertAtend(40)
llist.insertAtend(50)
  
llist.printLinkedList()
print()
llist.deleteNode(2)
llist.printLinkedList()

