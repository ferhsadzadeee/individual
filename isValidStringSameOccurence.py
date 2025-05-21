def isValid(s):
    from collections import Counter

    freq = Counter(s)
    values = list(freq.values())
    count = Counter(values)

    if len(count) == 1:
        return "YES"
    elif len(count) == 2:
        key1, key2 = count.keys()
        if (count[key1] == 1 and (key1 - 1 == key2 or key1 == 1)) or \
           (count[key2] == 1 and (key2 - 1 == key1 or key2 == 1)):
            return "YES"
    return "NO"