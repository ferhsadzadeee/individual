from collections import Counter


def happyLadybugs(b):
    count = Counter(b)

    for color, cnt in count.items():
        if color != '_' and cnt == 1:
            return "NO"

    if '_' not in count:
        for i in range(len(b)):
            if i > 0 and b[i] == b[i - 1]:
                continue
            if i < len(b) - 1 and b[i] == b[i + 1]:
                continue
            return "NO"
        return "YES"

    return "YES"


g = int(input())
for _ in range(g):
    n = int(input())
    b = input().strip()
    print(happyLadybugs(b))