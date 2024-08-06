# "Binary search or Half interval search Algorithm"


print("Binary Search Starts Here")
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

# Example usage
arr = [6, 12, 17, 23, 38, 45, 55, 77, 84, 90]
target = 45

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")
