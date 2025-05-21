def repeatedString(s, n):
    count_in_single = s.count('a')

    full_repeats = n // len(s)

    remainder = n % len(s)

    count_in_remainder = s[:remainder].count('a')

    total = full_repeats * count_in_single + count_in_remainder

    return total


s = input().strip()
n = int(input())
print(repeatedString(s, n))