def luckBalance(k, contests):
    important = []
    unimportant = []
    for l, t in contests:
        if t == 1:
            important.append(l)
        else:
            unimportant.append(l)

    important.sort(reverse=True)
    max_luck = sum(unimportant) + sum(important[:k]) - sum(important[k:])

    return max_luck


n, k = map(int, input().split())
contests = []
for _ in range(n):
    l, t = map(int, input().split())
    contests.append((l, t))

print(luckBalance(k, contests))