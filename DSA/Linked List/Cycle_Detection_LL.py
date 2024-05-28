## Floyd's Cycle detection Approach (Tortoise hare approach or slow fast approach)
## hare = 2 steps , Tortoise = 1 step
## if Hare == Tortoise -> loop Exist
## if Hare != Tortoise -> loop  not exist

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
    
    def DetectLoop(self):
        hare = self.head
        tortoise =self.head
        
        while hare and tortoise and hare.nextPtr:
            hare = hare.nextPtr.nextPtr
            tortoise = tortoise.nextPtr

            if hare == tortoise:
                return True
        return False
    # print the LL   
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.nextPtr
             
# Main Code
llist = LinkedList()
llist.insertAtend(10)
llist.insertAtend(20)
llist.insertAtend(30)
llist.insertAtend(40)
  
llist.head.nextPtr.nextPtr.nextPtr = llist.head  
if llist.DetectLoop():
    print("Loop exist in LL")
else:
    print("No Loop exist")