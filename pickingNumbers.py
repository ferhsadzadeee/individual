from collections import defaultdict


def pickingNumbers(a):
    frequency = defaultdict(int)
    max_length = 0
    for num in a:
        frequency[num] += 1
    for num in sorted(frequency.keys()):
        current_length = frequency[num]
        if num + 1 in frequency:
            current_length += frequency[num + 1]
        max_length = max(max_length, current_length)

    return max_length

n = int(input())
a = list(map(int, input().split()))
print(pickingNumbers(a))