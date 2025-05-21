def gameOfStones(n):
    if n % 7 in [0, 1]:
        return "Second"
    else:
        return "First"