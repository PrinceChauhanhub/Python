#Time COmplexity -> O(n)
    
def MaxAndMin(arr,i,j):
    ##for single element
    if i==j:
        max_val=arr[i]
        min_val=arr[i]
    ##for two elemtn
    elif i==j-1:
        if arr[i]<arr[j]:
            max_val=arr[j]
            min_val=arr[i]
        else:
            min_val=arr[j]
            max_val=arr[i]
    
    ##for more than two element
    else:
        #divide 
        mid=i+(j-i)//2
        #recursion -> conquer
        max_1,min_1=MaxAndMin(arr,i,mid)
        max_2,min_2=MaxAndMin(arr,mid+1,j)

        #combine 
        if max_1>max_2:
            max_val=max_1
        else:
            max_val=max_2
            
        if min_1 > min_2:
            min_val=min_2
        else:
            min_val=min_1
    
    return max_val,min_val
    
arr = [20,0,39,45,65,21,44,89,92]
i = 0
j = len(arr)-1
max_val,min_val = MaxAndMin(arr,i,j)
print("max value is :",max_val ,"and min value is:",min_val)