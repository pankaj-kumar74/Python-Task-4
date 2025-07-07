# Task 32: Find Subarray with Given Sum
def find_subarray_with_sum(arr, target):
    curr_sum = 0
    prefix_sum = {0: -1}
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum - target in prefix_sum:
            return (prefix_sum[curr_sum - target] + 1, i)
        prefix_sum[curr_sum] = i
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter array: ").split()))
    target = int(input("Enter target sum: "))
    result = find_subarray_with_sum(arr, target)
    print("Subarray indices:" if result != -1 else "Subarray not found:", result)
