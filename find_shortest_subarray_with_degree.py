def findShortestSubArray(nums):
    count = {}
    first_index = {}
    max_freq = 0
    min_len = float('inf')

    for i, num in enumerate(nums):
        if num not in first_index:
            first_index[num] = i
        count[num] = count.get(num, 0) + 1
        if count[num] > max_freq:
            max_freq = count[num]
            min_len = i - first_index[num] + 1
        elif count[num] == max_freq:
            min_len = min(min_len, i - first_index[num] + 1)

    return min_len