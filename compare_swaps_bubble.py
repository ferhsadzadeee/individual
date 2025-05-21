def bubble_sort_swaps(arr):
    n = len(arr)
    swap_count = 0
    a = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_count += 1
    return swap_count

def insertion_sort_swaps(arr):
    swap_count = 0
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            swap_count += 1
        a[j + 1] = key
    return swap_count

# Example usage
arr = [5, 1, 4, 2, 8]

bubble_swaps = bubble_sort_swaps(arr)
insertion_swaps = insertion_sort_swaps(arr)

print("Original array:", arr)
print("Bubble Sort swaps:", bubble_swaps)
print("Insertion Sort swaps:", insertion_swaps)
