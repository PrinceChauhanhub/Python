#problem name -  Two sum 
#time complexity : O(n)
#Two pointer approach
#array is sorted
def TwoSum (arr,target):
    right=len(arr)-1
    left=0
    while(left<right):
        val=arr[left]+arr[right]
        if(val==target):
            return(arr[left],arr[right])
        elif(val>target):
            right-=1
        else:
            left+=1
    return -1,-1

arr=[20,40,60,80,90,120,140]

target=210
ans=TwoSum(arr,target)
print(ans)