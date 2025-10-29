#linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#binary seearch
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

data = [64, 25, 12, 22, 11]
print("Original array:", data)

sorted_data = selection_sort(data.copy())
print("Sorted array (Selection Sort):", sorted_data)

target = 22
index_linear = linear_search(data, target)
print(f"Linear Search: Element {target} found at index {index_linear}" if index_linear != -1 else f"Linear Search: Element {target} not found")

index_binary = binary_search(sorted_data, target)
print(f"Binary Search: Element {target} found at index {index_binary}" if index_binary != -1 else f"Binary Search: Element {target} not found")