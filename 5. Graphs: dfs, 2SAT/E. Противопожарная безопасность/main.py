def data_input():
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


def kosaraju(V, G, G_inv):
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

# colors [011220132]
# c      [123456789]

# if компонентна связности не смотрит никуда, кроме себя, то это и есть сток

# запустить dfs от каждой ксс, если все они компоненты из 1 ксс, то это сток

# get indices of a first appearance with element

def get_ans(c, colors, G):
    marked_ccs = [1] * c

    for i in G:
        for j in G[i]:
            if colors[i] != colors[j]:
                marked_ccs[colors[i]] = 0

    # print(marked_ccs)  # наши стоки, как ксс.
    # Выбрать в них по 1 вершине

    # get indices that are non-0
    ccs = list()
    for i, c in enumerate(marked_ccs):
        if c == 1:
            ccs.append(i)

    ans = list()
    for i, c in enumerate(colors):
        if c in ccs:
            ccs.remove(c)
            ans.append(i)
    return ans


def main():
    V, E, G, G_inv, edges = data_input()

    colors, c = kosaraju(V, G, G_inv)

    ans = get_ans(c, colors, G)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    import sys, threading

    sys.setrecursionlimit(10000)
    threading.stack_size(2 ** 25)
    thread = threading.Thread(target=main)
    thread.start()
