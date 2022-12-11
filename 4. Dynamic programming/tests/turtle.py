n, m = list(map(int, input().split()))
matrix = list()
i = n
while i > 0:
    matrix.append(list(map(int, input().split())))
    i -= 1

d = [[0] * (m) for _ in range(n)]

d[0][0] = matrix[0][0]

for i in range(1, m):
    d[0][i] = d[0][i - 1] + matrix[0][i - 1]

for j in range(1, n):
    d[j][0] = d[j - 1][0] + matrix[j][0]

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = matrix[i][j]
        d[i][j] += min(d[i - 1][j], d[i][j - 1])

print(d[n - 1][m - 1])
