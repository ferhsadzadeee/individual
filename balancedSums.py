def balancedSums(arr):
    total = sum(arr)
    left_sum = 0

    for num in arr:
        if left_sum == total - left_sum - num:
            return "YES"
        left_sum += num

    return "NO"

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(balancedSums(arr))


if __name__ == "__main__":
    main()