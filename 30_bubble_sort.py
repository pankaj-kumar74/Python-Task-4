# Task 30: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
    print("Sorted array:", bubble_sort(arr))
