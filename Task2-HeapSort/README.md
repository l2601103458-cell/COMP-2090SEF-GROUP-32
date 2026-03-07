# Self Study Report on Heap Sort

## 1. Introduction
Sorting is a fundamental operation in computer science, widely used in data processing, information retrieval, and artificial intelligence, and heap sort is an efficient sorting algorithm based on the heap data structure, with stable time complexity and low space overhead. This report introduces the heap data structure, explains the principle of heap sort, provides a Python implementation, analyzes its complexity, and discusses applications.

## 2. Fundamental Concepts: Heap Data Structure
### 2.1 What is a Heap?
A heap is a complete binary tree that satisfies the heap property:
- **Max-heap**: The value of a parent node is always greater than or equal to its children nodes. The root node is the maximum value.
- **Min-heap**: The value of a parent node is always less than or equal to its children nodes. The root node is the minimum value.

Heaps can be efficiently stored in an array using index mapping:
For a node at index i:
- Left child: 2*i + 1
- Right child: 2*i + 2
- Parent: (i-1) // 2

### 2.2 Core Operations of Heap
- **Heapify**: Adjusts a subtree to maintain the heap property. Given a node index, it compares the node with its children, swaps if necessary, and recursively fixes the affected subtree.
- **Build Heap**: Converts an unsorted array into a heap by applying heapify to all non-leaf nodes starting from the last one up to the root.

### 2.3 Principle of Heap Sort
Heap sort leverages the max-heap property to sort data in-place. The algorithm follows these steps:
1. Build a max-heap from the input array. The largest element is now at the root.
2. Swap the root (maximum value) with the last element of the heap. This places the largest element in its correct sorted position at the end of the array.
3. Reduce the heap size by 1 (excluding the last element which is now sorted).
4. Heapify the new root to restore the max-heap property for the remaining elements.
5. Repeat steps 2-4 until the entire array is sorted.

### 2.4 Code Example
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    test_data = [12, 11, 17, 5, 6, 8]
    print("Original array:", test_data)
    sorted_data = heap_sort(test_data)
    print("Sorted array:", sorted_data)
