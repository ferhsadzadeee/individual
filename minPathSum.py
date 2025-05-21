def minPathSum(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[-1]