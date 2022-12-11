from collections import deque


def find_cc(V, adj):
    colors = [-1] * (V + 1)
    color = 0

    stack = deque()

    for v in range(1, V + 1):
        if colors[v] == -1:
            color += 1
            stack.clear()
            stack.append(v)
            while stack:
                v = stack.pop()

                if colors[v] != -1:
                    continue

                colors[v] = color

                adjlist = adj[v]

                for i in range(len(adjlist)):
                    u = adjlist[i]
                    if colors[u] == -1:
                        stack.append(u)
    return colors
