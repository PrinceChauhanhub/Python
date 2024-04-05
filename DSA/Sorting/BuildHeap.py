import heapq

def heapify(arr):
    n = len(arr)

    # Start from the last non-leaf node and heapify down to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, i, n)

def heapify_down(arr, idx, heap_size):
    smallest = idx
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2

    # Check if left child is smaller than parent
    if left_child < heap_size and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Check if right child is smaller than parent or left child
    if right_child < heap_size and arr[right_child] < arr[smallest]:
        smallest = right_child

    # If smallest is not the parent, swap parent with smallest and heapify down
    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        heapify_down(arr, smallest, heap_size)

# Example usage:
arr = [1,2,3,4,5,6,7,8,9,10]

# Convert the list into a min-heap
heapify(arr)

print("Min-Heap:", arr)  # Output: [1, 3, 4, 7, 9, 5]
