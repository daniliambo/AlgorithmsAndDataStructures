def data_input():
    import sys
    V = int(input())
    E = int(input())

    out_list = [0] * (V + 1)
    inlist = [0] * (V + 1)

    edges = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
    G = {}
    G_inv = {}
    for i in range(1, V + 1):
        G[i] = set()
        G_inv[i] = set()
    for edge in edges:
        if edge[0] in G.keys():

            out_list[edge[0]] = out_list[edge[0]] + 1
            inlist[edge[1]] = out_list[edge[1]] + 1

            G[edge[0]].add(edge[1])
            G_inv[edge[1]].add(edge[0])
        else:
            G[edge[0]] = edge[1]
            G_inv[edge[0]] = edge[1]

            out_list[edge[0]] = out_list[edge[0]] + 1
            inlist[edge[1]] = out_list[edge[1]] + 1

    print(inlist, 'inlist')
    print(out_list, 'ouput_list')

    return V, E, G, G_inv, edges


V, E, G, G_inv, edges = data_input()
print(G)
