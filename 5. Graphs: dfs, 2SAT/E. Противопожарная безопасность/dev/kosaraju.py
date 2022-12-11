def main(V, G, G_inv):
    colors = [-1] * (V + 1)
    used = [-1] * (V + 1)
    ts = list()
    c = 0

    def dfs(v):
        used[v] = 1
        for u in G[v]:
            if used[u] == -1:
                dfs(u)
        ts.append(v)

    for v in range(1, V + 1):
        if used[v] == -1:
            dfs(v)

    ts.reverse()

    def dfs2(v):
        colors[v] = c
        for u in G_inv[v]:
            if colors[u] == -1:
                dfs2(u)

    for v in ts:
        if colors[v] == -1:
            dfs2(v)
            c += 1
    return colors, c
