
#time Complexity : O(n)
#Space Complexity : O(1)

def linearsearch(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1
arr=[20,45,27,47,55,67,75,88,90]
x=67
result=linearsearch(arr,x)
print ("element is found at index :",result) 