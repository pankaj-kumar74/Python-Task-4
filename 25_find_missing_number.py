# Task 25: Find Missing Number
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers (space-separated): ").split()))
    print("Missing number:", find_missing_number(arr))
