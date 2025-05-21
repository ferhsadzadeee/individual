def gameOfThrones(s):
    from collections import Counter
    counts = Counter(s)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"