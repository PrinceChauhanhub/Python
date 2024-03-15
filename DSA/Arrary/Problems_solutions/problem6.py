#square root of a number using binary search
#Time Complexity -> O(log n)
#Space Complexity -> O(1)  Linear

def SquareRoot(number):
    start = 0
    end = number
    while (start <= end):
        mid = start + (end-start) // 2
        if((mid*mid)==number):
            ans= mid
            break
        elif((mid*mid) > number):
            end=mid-1
            ans=mid-1
        else:
            start=mid+1
            ans=mid
            
    increment=0.1
    for i in range(0,3):
        while(ans*ans<=number):
            ans+=increment
            
        ans-=increment
        increment=increment/10
    return int(ans) 

n=int(input("enter the number :"))
ans=SquareRoot(n)
print("the square root of number is :",ans)