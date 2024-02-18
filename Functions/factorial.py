#factorial of a number

def fact(n):
    if (n==0):
        return 1
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

n=int(input("enter the number :"))
output=fact(n)

print("the factorial is ",output)