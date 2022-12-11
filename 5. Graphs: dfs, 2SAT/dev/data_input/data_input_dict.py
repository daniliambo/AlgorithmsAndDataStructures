import sys

V, E = list(map(int, input().split()))

edges = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
print(edges)
G = {}
for i in range(1, V + 1):
    G[i] = set()

for edge in edges:
    if edge[0] in G.keys():
        G[edge[0]].add(edge[1])
    else:
        G[edge[0]] = edge[1]
print(G)
