def solve_sat(n, test):
    # imports
    from build_graph import build_graph
    from kosaraju import kosaraju
    G, G_inv = build_graph(n, test)

    # kosaraju
    V = len(G.keys())
    colors, c = kosaraju(V, G, G_inv)
    # print(colors)

    ans = list()
    for i in range(2, 2 * n + 1, 2):
        if colors[i - 1] > colors[i]:
            ans.append(1)
        else:
            ans.append(0)
    print(''.join([str(x) for x in ans]))
