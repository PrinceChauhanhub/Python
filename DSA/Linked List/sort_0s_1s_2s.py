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
    
    def sort012(self):
        if self.head is None or self.head.nextPtr is None:
            return head
        
        count0 = 0
        count1 = 0
        count2 = 0
        temp = self.head
        while temp:
            if temp.data == 0:
                count0+=1
            elif temp.data == 1:
                count1+=1
            else:
                count2+=1
            temp = temp.nextPtr  
        temp = self.head
        while temp:
            if count0>0:
                temp.data = 0
                count0-=1
            elif count1>0:
                temp.data =1
                count1-=1
            else:
                temp.data = 2
                count2-=1
            temp = temp.nextPtr 
        
        
        
    # print the LL   
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.nextPtr
             
# Main Code
llist = LinkedList()
llist.insertAtend(1)
llist.insertAtend(0)
llist.insertAtend(1)
llist.insertAtend(2)
llist.insertAtend(0)
  
llist.printLinkedList()

llist.sort012()
print("\n")
llist.printLinkedList()
