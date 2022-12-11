import sys

inf = float('inf')

n, m, f = map(int, sys.stdin.readline().split())

dist_matrix = [[inf] * n for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n): dist_matrix[i][i] = 0

next = [[0, 0] * n for _ in range(n)]
print(next, 'next')
# [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
# init graph
for i in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    if -data[2] < dist_matrix[data[0] - 1][data[1] - 1]:
        dist_matrix[data[0] - 1][data[1] - 1] = -data[2]
        next[data[0] - 1][data[1] - 1] = [data[1] - 1, i + 1]
        graph[data[0] - 1].append(data[1] - 1)


def dfs(start, used, d, cycle, graph=graph):  # найти положительные циклы
    que = [start]

    while que:
        u = que.pop()
        if u in used:
            continue
        if d[u][u] < 0:
            cycle.add(u)

        used.add(u)
        for v in graph[u]:
            que.append(v)


def dfs1(start, used, end, cycle, graph=graph):  # можно ли из этого цикла добраться до последней вершины
    global inf_bool
    que = [start]

    while que:
        u = que.pop()
        if u in used:
            continue
        if u == end:
            inf_bool = True
        if u in cycle:
            cycle.discard(u)

        used.add(u)
        for v in graph[u]:
            que.append(v)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist_matrix[j][k] > dist_matrix[j][i] + dist_matrix[i][k]:
                dist_matrix[j][k] = dist_matrix[j][i] + dist_matrix[i][k]
                next[j][k] = next[j][i]  #

cities = list(map(int, sys.stdin.readline().split()))

inf_bool = False

used = set()
cycle = set()
dfs(cities[0] - 1, used, dist_matrix, cycle)

while cycle:
    u = cycle.pop()
    used = set()
    dfs1(u, used, cities[f - 1] - 1, cycle)
    if inf_bool == True:
        break

if inf_bool:
    print('infinitely kind')
else:
    ans = []
    for i in range(f - 1):
        l = cities[i] - 1
        r = cities[i + 1] - 1

        while l != r:
            l, flight = next[l][r]
            ans.append(flight)

    print(len(ans))
    print(*ans)
