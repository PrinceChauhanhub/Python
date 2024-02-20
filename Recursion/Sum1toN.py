#sum from 1 to N

def Sum1toN(n):
    if(n==1):
        return 1
    return n + Sum1toN(n-1)

n=int(input("enter the number :"))
print("the sum is :",Sum1toN(n))