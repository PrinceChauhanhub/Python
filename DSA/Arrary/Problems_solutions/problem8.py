#checks a number is perfect square or not
#Time Complexity -> O(log n)
#Space Complexity -> O(1)

def PerfectSquare(n):
    start=0
    end=n
    while(start<=end):
        mid=start+(end-start)//2
        
        if((mid*mid) == n):
            return True
        elif((mid*mid)>n):
            end=mid-1
        else:
            start=mid+1
    return False

n=int(input("ENter the number: "))
print(PerfectSquare(n))