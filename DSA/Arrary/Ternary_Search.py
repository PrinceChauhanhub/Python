#ternary_Search
#Time Complexity ->
#Space Complexity ->

def Ternary_Search(arr,start,end,target):
    while(start<=end):
        mid1=start+(end-start)//2
        mid2=end-(end-start)//2
        
        if(arr[mid1]==target):
            return mid1
        if(arr[mid2]==target):
            return mid2
        elif(arr[mid1]>target):
            return Ternary_Search(arr,start,mid1-1,target)
        elif(arr[mid2]<target):
            return Ternary_Search(arr,mid2+1,end,target)
        else:
            return Ternary_Search(arr,mid1+1,mid2-1,target)
            
    return -1
    
    
arr=[20,25,47,56,59,63,65,79,82]
target=59
start=0
end=len(arr)-1
print(Ternary_Search(arr,start,end,target))