n, m = map(int, input().split())


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


edges = []
for _ in range(m):
    b, e, w = map(int, input().split())
    edges.append((b, e, w))
edges.sort(key=lambda x: x[2])
parent = list(range(n + 1))
rank = [0 for _ in range(n + 1)]
cnt = 0
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        cnt += edge[2]
        union(edge[0], edge[1])
print(cnt)
