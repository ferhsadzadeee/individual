def migratoryBirds(arr):
    freq = [0] * 6
    for bird in arr:
        freq[bird] += 1
    max_freq = max(freq)
    for i in range(1, 6):
        if freq[i] == max_freq:
            return i