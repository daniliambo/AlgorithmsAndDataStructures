def data_input():
    import sys
    V = int(input())
    E = int(input())
    edges = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
    G = {}
    G_inv = {}
    for i in range(1, V + 1):
        G[i] = set()
        G_inv[i] = set()
    for edge in edges:
        if edge[0] in G.keys():
            G[edge[0]].add(edge[1])
            G_inv[edge[1]].add(edge[0])
        else:
            G[edge[0]] = edge[1]
            G_inv[edge[0]] = edge[1]

    return V, E, G, G_inv, edges
