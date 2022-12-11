a = [2, 3, 2, 1, 5, 2, 6, 24, 9]
n = len(a)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
mx = max(dp)
ans = list()
i = n - 1

while mx > 0:
    if dp[i] == mx:
        ans.append(i)
        mx = mx - 1
    i = i - 1
print(*ans[::-1])
