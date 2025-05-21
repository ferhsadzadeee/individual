def minimumDistances(a):
    last_seen = {}
    min_distance = float('inf')
    for i, value in enumerate(a):
        if value in last_seen:
            min_distance = min(min_distance, i - last_seen[value])
        last_seen[value] = i
    return min_distance if min_distance != float('inf') else -1