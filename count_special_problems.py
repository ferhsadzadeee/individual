def workbook(n, k, arr):
    special_count = 0
    page = 1
    for problems in arr:
        for i in range(1, problems + 1, k):
            end = min(i + k - 1, problems)
            if page >= i and page <= end:
                special_count += 1
            page += 1
    return special_count