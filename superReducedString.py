def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Aynı karakter varsa çıkar (çiftleri sil)
        else:
            stack.append(char)  # Farklıysa yığına ekle
    return ''.join(stack) if stack else "Empty String"


print(superReducedString("aaabccddd"))
print(superReducedString("aa"))
print(superReducedString("baab"))