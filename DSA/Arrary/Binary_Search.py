#recursive approach 

def binarySearch(arr,start,end,x):
    while(start<=end):
        mid = start +(end - start) // 2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return binarySearch(arr,mid+1,end,x)
        else:
            return binarySearch(arr,start,mid-1,x)
    return -1

arr=[10,20,30,40,50,60,70]
x=70
end=len(arr)
ans = binarySearch(arr,0,end-1,x)
print("Element found at index:",ans)



#Iterative Approach

# def BinarySearch(arr,x,start,end):
#     while start<=end:
#         mid=start+(end-start)//2
        
#         if(arr[mid]==x):
#             return mid
#         elif(arr[mid]<x):
#             start=mid+1
#         else:
#             end=mid-1
#     return -1  
# arr=[10,20,30,40,50,60,70,80,90]
# x=70
# answer=BinarySearch(arr,x,0,len(arr)-1)
# print("The value is at index :",answer)