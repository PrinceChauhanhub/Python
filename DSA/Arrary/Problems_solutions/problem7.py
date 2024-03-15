#u are a product manager new products are developed from the previous one all the versions after bad are also bad
#Time Complexity -> O(log n)
#Space Complexity -> O(1)

def BadVersion(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start)//2
        if(arr[mid]==1):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans            
            
arr=[0,0,0,0,0,0,1,1,1]
answer=BadVersion(arr)
print("ans is: ",answer)