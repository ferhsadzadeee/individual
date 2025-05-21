def reverseWords(s: str) -> str:
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
print(reverseWords("Let's take LeetCode contest"))