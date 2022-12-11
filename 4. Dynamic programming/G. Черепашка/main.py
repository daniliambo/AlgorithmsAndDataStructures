# input
n, m = map(int, input().split())
arr = [[0] * m for i in range(n)]
for i in range(0, n):
    arr[i] = [int(i) for i in input().split()]

# init
d = [[0] * m for i in range(n)]
d[0][0] = arr[0][0]

# 1st row/col
for i in range(1, n):
    d[i][0] = d[i - 1][0] + arr[i][0]
for j in range(1, m):
    d[0][j] = d[0][j - 1] + arr[0][j]

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = min(d[i - 1][j], d[i][j - 1]) + arr[i][j]

print(d[n - 1][m - 1])
