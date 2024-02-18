#pass by value

def  addOne(x):
    x=x+1
    print("inside function",x) 
    
x=5
addOne(x)
print("outside function:",x)

#pass by reference
def ModifyList(lst):
    lst.append(4)
    print("inside function:",lst)
    
lst=[1,2,3]
ModifyList(lst)
print("outside function:",lst)