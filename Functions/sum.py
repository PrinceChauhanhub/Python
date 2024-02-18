#sum of n numbers

def sum(n):
    val=0
    for i in range(1,n+1):
        val=val+i
        
    return val

n=int(input("entet n:"))
res=sum(n)
print("the sum is :",res)  