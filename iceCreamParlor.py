def icecreamParlor(m, cost):
    seen = {}

    for i, price in enumerate(cost, start=1):
        complement = m - price
        if complement in seen:
            return sorted([seen[complement], i])
        seen[price] = i

    return []


def main():
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        cost = list(map(int, input().split()))
        result = icecreamParlor(m, cost)
        print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()