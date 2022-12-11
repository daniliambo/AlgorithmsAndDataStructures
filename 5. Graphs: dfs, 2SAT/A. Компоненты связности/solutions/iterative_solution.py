from collections import defaultdict
def dfs(G, v, mrk):
    global mark
    stack = []
    mark[v] = mrk
    stack.append(iter(G[v]))
    while stack:
        vrt = next(stack[-1], None)
        if vrt is not None:
            if not mark[vrt]:
                mark[vrt] = mrk
                stack.append(iter(G[vrt])) 
        else: stack.pop()
N, M = map(int, input().split())
G = defaultdict(set)
mark = [0]*(N + 1)
mrk = 0
for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
for i in range(1, N + 1):
    if not mark[i]:
        mrk += 1
        dfs(G, i, mrk)
print(mrk)
print(*mark[1::])






