# O(n^2), можно за O(nlogn)

n = int(input())
a = list(map(int, input().split()))
# a = [2, 3, 2, 1, 5, 2, 6, 24, 9]
n = len(a)
dp = [1] * n
res = [-1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            res[i] = j
ans = list()
mx = 0
for i in range(1, n):
    if mx < dp[i]:
        mx_index = i
        mx = dp[i]

# print(mx, mx_index)

# restore indices
print(mx)
while mx > 0:
    ans.append(mx_index)
    mx_index = res[mx_index]
    mx = mx - 1

# restore symbols
# print(*ans[::-1])
print(*[a[i] for i in ans[::-1]])
