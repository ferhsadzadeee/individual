def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            right.append(x)

    return left + equal + right