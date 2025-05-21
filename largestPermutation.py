def largestPermutation(k, arr):
    n = len(arr)
    pos = {value: idx for idx, value in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        max_val = n - i
        if arr[i] != max_val:
            max_idx = pos[max_val]
            pos[arr[i]] = max_idx
            pos[max_val] = i
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            k -= 1
    return arr