#factorial of number using recursion

def fact(n):
    
    #base case
    if(n==0):
        return 1
    
    #recursive case
    return (n*fact(n-1))

n=int(input("enter the number:"))
print("the factorial is :",fact(n))