# То же самое, что и НОП, только для возрастающих
a = [2, 100, 1, 100, 3]
b = [10, 10, 2, 1, 3, 10]  # НОП: 2,1,3 # НОВП: 1, 3
# https://neerc.ifmo.ru/wiki/index.php?title=Задача_о_наибольшей_общей_возрастающей_последовательности
n = len(a)
m = len(b)
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if a[i - 1] == b[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

print(dp[n][m])
