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
     
    # print the LL   
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.nextPtr
    
    # reverse the singly linked list
    
    def reverseList(self):
        prev = None
        next = None
        curr = self.head
        
        while curr:
            next = curr.nextPtr    # next = 20
            curr.nextPtr = prev    # 10 points to null                   (process contineous till end of loop)
            prev = curr            # prev = 10
            curr = next            # curr =20
            
        # Update the head pointer
        self.head = prev
         
# Main Code
llist = LinkedList()
llist.insertAtend(10)
llist.insertAtend(20)
llist.insertAtend(30)
llist.insertAtend(40)
llist.insertAtend(50)
  
llist.printLinkedList()

llist.reverseList()
print()
print("Reversal of Linkled list is ",end =" ")
llist.printLinkedList()