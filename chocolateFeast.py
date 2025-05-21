def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = chocolates

    while wrappers >= m:
        exchanged = wrappers // m
        chocolates += exchanged
        wrappers = wrappers % m + exchanged

    return chocolates


t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    print(chocolateFeast(n, c, m))