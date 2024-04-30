#create a build heap method that returns a minheap

def build_heap(arr):
    n=len(arr)
    for i in range(n//2-1,-1-1):
        heapify_down(arr,i,n)
    return arr

def heapify_down(arr,i,n):
    smallest=i
    left_child=2*i+1
    right_child=2*i+2
    
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] <arr[smallest]:
        smallest = right_child
    
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify_down(arr,smallest,n)

arr=[1,3,7,8,9,10,12,16,18,2,27]
min_heap = build_heap(arr)
print(min_heap) 