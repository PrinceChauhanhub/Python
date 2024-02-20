# a raised to power b with recursion

def pow(a,b):
    
    if(b==0):
        return 1
    
    val=a * pow(a,b-1)
    return val

a=int(input("enter a:"))
b=int(input("enter b:"))

print("a raised to power b is ",pow(a,b))