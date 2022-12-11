import sys, threading


# build graph

def build_graph(n, test):
    # init
    G = dict()
    G_inv = dict()

    # fill with empty sets
    for i in range(1, 2 * n + 1):
        G[i] = set()
        G_inv[i] = set()

    # build graph
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


# kosaraju

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


# solve sat

def solve_sat(n, test):
    # imports
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


# process tests


def process_tests():
    content = sys.stdin.read().splitlines()
    l = len(content)
    i = 0
    while i < l:
        test = list()
        n, m = list(map(int, content[i].split()))
        while m > 0:
            i += 1
            x = list(map(int, content[i].split()))
            x[0] += 1
            x[2] += 1
            test.append(x)
            m -= 1
        i += 1
        solve_sat(n, test)


def main():
    process_tests()


if __name__ == "__main__":
    sys.setrecursionlimit(1500000)
    threading.stack_size(2 ** 23)
    thread = threading.Thread(target=main)
    thread.start()
