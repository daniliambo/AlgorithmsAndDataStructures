from collections import defaultdict
def dfs(G, v):
    global mark
    stack = []
    mark[v] = 1
    stack.append([mark[v], iter(G[v])])
    while stack:
        clr, vrt = stack[-1][0], next(stack[-1][1], None)
        if vrt is not None:
            if not mark[vrt]:
                mark[vrt] = 2 if clr == 1 else 1
                stack.append([mark[vrt], iter(G[vrt])]) 
            else:
                if mark[vrt] == clr:
                    return False
                else: continue
        else: stack.pop()
    return True
N, M = map(int, input().split())
G = defaultdict(set)
mark = [0]*(N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
for i in range(1, N + 1):
    if not mark[i]:
        if not dfs(G, i):
            print('NO')
            break
else:
    print('YES')