def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    si = 0
    ei = len(arr)-1
    while si <= ei:
        mid = si + (ei - si) // 2
        midVal = arr[mid]
        if midVal == target:
            return mid
        elif target < midVal:
            ei = mid - 1
        else:
            si = mid + 1

    return -1  # not found
