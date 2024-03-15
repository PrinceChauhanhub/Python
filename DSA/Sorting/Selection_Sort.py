#Time Complexity -> O(n^2)
#space Complexity -> O(1)

def Selection_Sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    
    return arr
            
        
#Driver Code        
arr=[70,20,50,30,90,5,15]    
result=Selection_Sort(arr)
print("Array after sorting:",result)
    
