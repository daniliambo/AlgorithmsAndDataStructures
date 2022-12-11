a = [4, 2, 3, 2, 1, 5, 2, 6, 24, 9]
n = len(a)
dp = [1] * n
ans = list()
mx = 0

# create dp
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# look for mx and mx_index
for i in range(1, n):
    if mx < dp[i]:
        mx_index = i
        mx = dp[i]

# restore answer
ans.append(a[mx_index])
i = mx_index - 1
while mx > 0:
    if a[mx_index] > a[i] and mx == dp[i] + 1:
        ans.append(a[i])
        mx_index = i
        mx = mx - 1
    if i > 0:
        i = i - 1
    else:
        break

print(*ans[::-1])
