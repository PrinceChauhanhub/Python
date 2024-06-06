#checking palindrome in linked list using stack

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
    
    def isPalindrome(self):
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.nextPtr
        temp = self.head
        for i in range(len(stack)//2):
            stack_ele = stack.pop()
            if stack_ele == temp.data:
                temp=temp.nextPtr
                continue
            else:
                return 0
        return 1
        
            
        
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
llist.insertAtend(0)
llist.insertAtend(10)
  
if llist.isPalindrome():
    print("palindrome")
else:
    print("not palindrome")