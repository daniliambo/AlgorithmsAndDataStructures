n, m, k = map(int, input().split())


def path_count(u, v):
    global p
    cnt = 0
    while u != v:
        u = p[u][v][0]
        cnt += 1
    return cnt


def path(u, v):
    path = []
    while u != v:
        path.append(p[u][v][1])
        u = p[u][v][0]
    return path


d = [[float('-inf') for _ in range(n + 1)] for _ in range(n + 1)]
p = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    d[i][i] = 0
for i in range(m):
    b, e, w = map(int, input().split())
    d[b][e] = w
if d[b][e] < w:
    p[b][e], p[e][e], p[b][b] = [e, i + 1], [e, 0], [b, 0]

cities = list(map(int, input().split()))

for l in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][j] < d[i][l] + d[l][j]:
                d[i][j] = d[i][l] + d[l][j]
                p[i][j] = p[i][l]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for t in range(1, n + 1):
            if d[i][t] > float('-inf') and d[t][t] != 0 and d[t][j] > float('-inf'):
                d[i][j] = float('inf')

cnt = 0

for i in range(1, len(cities)):
    if d[cities[i - 1]][cities[i]] == float('inf'):
        print('infinitely kind')
        break
    else:
        cnt += path_count(cities[i - 1], cities[i])
else:
    print(cnt)
    for i in range(1, len(cities)):
        print(*path(cities[i - 1], cities[i]), end=' ')
