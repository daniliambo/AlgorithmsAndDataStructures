from math import sqrt

def find(v):
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

n = int(input())
coord = []
edges = []
for _ in range(n):
    coord.append(tuple(map(int, input().split())))
for i in range(len(coord) - 1):
    for j in range(1, len(coord)):
        edges.append(
            (i + 1, j + 1, sqrt((coord[i][0] - coord[j][0]) ** 2 
                                + (coord[i][1] - coord[j][1]) ** 2))
        )
edges.sort(key=lambda x: x[2])
parent = list(range(n + 1))
rank = [0 for _ in range(n + 1)]
coord = []
cnt = 0
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        cnt += edge[2]
        coord.append((edge[0], edge[1]))
        union(edge[0], edge[1])
print(cnt)
print(len(coord))
for elem in coord:
    print(*elem)
