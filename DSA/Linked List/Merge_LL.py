# Time Complexity -> O(n)
# Merge two sorted Linked List in Sorted Order
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
# merge two Sorted Linked List
def MergeLists(head1,head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        temp =head1
        temp.nextPtr = MergeLists(head1.nextPtr,head2)
    else:
        temp = head2
        temp.nextPtr = MergeLists(head1,head2.nextPtr)
    
    return temp
      
      
# Main Code
llist1 = LinkedList()
llist1.insertAtend(10)
llist1.insertAtend(20)
llist1.insertAtend(30)
llist1.insertAtend(40)
llist1.insertAtend(50) 
print("Linked list 1:")
     
llist1.printLinkedList()
print(" ")

llist2 = LinkedList()
llist2.insertAtend(11)
llist2.insertAtend(22)
llist2.insertAtend(33)
llist2.insertAtend(44)
llist2.insertAtend(55) 

print("Linked list 2:")     
llist2.printLinkedList()
print()

llist3 = LinkedList()
llist3.head =  MergeLists(llist1.head,llist2.head)
print("Merged Linked List:")
llist3.printLinkedList()