import sys, threading


def main():
    def data_input():
        import sys
        V, E = list(map(int, input().split()))
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

    def main():
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

    V, E, G, G_inv, edges = data_input()

    counter = 0
    count = set()

    cid = [-1] * (V + 1)
    no = 0

    colors, c = main()

    for edge in edges:
        if colors[edge[0]] == colors[edge[1]]:
            continue
        if (colors[edge[0]], colors[edge[1]]) not in count and (colors[edge[0]], colors[edge[1]])[::-1] not in count:
            count.add((colors[edge[0]], colors[edge[1]]))
            counter += 1

    print(counter)
    # for i in G:
    #     for j in G[i]:
    #         if colors[i] != colors[j]:
    #             count.add((colors[i], colors[j]))

    # print(len(count))


if __name__ == "__main__":
    sys.setrecursionlimit(1500000)
    threading.stack_size(2 ** 23)
    thread = threading.Thread(target=main)
    thread.start()
