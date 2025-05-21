def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p - d, m)
    return count
