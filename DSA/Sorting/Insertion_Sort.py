#Insertion Sort
#Time Complexity -> O(n^2 )
#Space Complexity -> O()

def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
         
        while (j>=0) and (arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
    return arr
    

arr=[75,90,100,95,85,80]
sorted_array=Insertion_Sort(arr)
print("The sorted array",sorted_array)