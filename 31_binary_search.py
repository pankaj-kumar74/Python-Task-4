# Task 31: Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted list: ").split()))
    target = int(input("Enter target: "))
    result = binary_search(arr, target)
    print("Found at index:" if result != -1 else "Not found:", result)
