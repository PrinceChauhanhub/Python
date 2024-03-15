#Time Complexity -> O(n^2)
#space Complexity -> O(1)

def BubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[70 , 20 , 50 , 60 , 35 , 70]
result=BubbleSort(arr)
print("The array after sorting\n",result)