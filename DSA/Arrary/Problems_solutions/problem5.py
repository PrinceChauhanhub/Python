#Binary Search in 2-D Array\
#Time Complexity - O()

def search2DArray(arr,target):
    m=len(arr)         ##len of  columns
    if m==0:
        return False

    n=len(arr[0])
    left,right=0,m*n-1
    
    #binary Search Implementation
    while left<=right:
        mid=left+(right-left)//2
        mid_element=arr[mid//n][mid%n]
        if target==mid_element:
            return True
        elif target < mid_element:
            right = mid-1
        else:
            left = mid+1
    return False
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=32
result=search2DArray(arr,target)
print(result)