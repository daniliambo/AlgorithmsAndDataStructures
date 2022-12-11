def build_graph(n, test):
    # init
    G = dict()
    G_inv = dict()

    # fill with empty sets
    for i in range(1, 2 * n + 1):
        G[i] = set()
        G_inv[i] = set()

    # fill graph
    for t in test:
        if t[1]:
            if t[3]:
                G[2 * t[0]].add(2 * t[2] - 1)
                G[2 * t[2]].add(2 * t[0] - 1)
            else:
                G[2 * t[0]].add(2 * t[2])
                G[2 * t[2] - 1].add(2 * t[0] - 1)
        else:
            if t[3]:
                G[2 * t[0] - 1].add(2 * t[2] - 1)
                G[2 * t[2]].add(2 * t[0])
            else:
                G[2 * t[0] - 1].add(2 * t[2])
                G[2 * t[2] - 1].add(2 * t[0])

    # build G_inv
    for v in G.keys():
        for u in G[v]:
            G_inv[u].add(v)

    # return
    return G, G_inv
