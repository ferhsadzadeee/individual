
def alternate(s):
    letters = list(set(s))
    max_length = 0

    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            l1 = letters[i]
            l2 = letters[j]

            filtered = [x for x in s if x == l1 or x == l2]

            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break

            if valid:
                max_length = max(max_length, len(filtered))

    return max_length