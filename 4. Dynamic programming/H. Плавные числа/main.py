n = int(input())

dp = [[0] * 10 for i in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]
        if j <= 8:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] += dp[i - 1][j]

print(sum(dp[n - 1]))
