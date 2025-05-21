import string

def caesarCipher(s, k):
    k = k % 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    shifted_lower = lower[k:] + lower[:k]
    shifted_upper = upper[k:] + upper[:k]

    translation_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)

    return s.translate(translation_table)

if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())
    print(caesarCipher(s, k))

# if __name__ == "__main__":
#     try:
#         n = int(input("Enter length of the string: "))  # Optional prompt
#         s = input("Enter the string: ")
#         k = int(input("Enter the shift value: "))
#         print(caesarCipher(s, k))
#     except Exception as e:
#         print("Invalid input:", e)