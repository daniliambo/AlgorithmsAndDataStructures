from sys import stdin
import sys
import threading


def main():
    def make_graph(n, m, statements):
        adj = [[] for i in range(2 * n)]
        rev_adj = [[] for i in range(2 * n)]
        for i in range(m):
            adj[statements[i][0] * 2 + statements[i][1]].append(statements[i][2] * 2 + (statements[i][3] + 1) % 2)
            adj[statements[i][2] * 2 + statements[i][3]].append(statements[i][0] * 2 + (statements[i][1] + 1) % 2)
            rev_adj[statements[i][2] * 2 + (statements[i][3] + 1) % 2].append(statements[i][0] * 2 + statements[i][1])
            rev_adj[statements[i][0] * 2 + (statements[i][1] + 1) % 2].append(statements[i][2] * 2 + statements[i][3])
        return (adj, rev_adj)

    def find_scc(adj, rev_adj, n):
        def dfs(v, order):
            used[v] = True
            for u in adj[v]:
                if not used[u]:
                    dfs(u, order)
            order.append(v)

        def dfs2(v, c):
            used[v] = True
            colors[v] = c
            for u in rev_adj[v]:
                if not used[u]:
                    if colors[u] == 0:
                        dfs2(u, c)

        used = [False] * (n)
        order = []
        for i in range(n):
            if not used[i]:
                dfs(i, order)

        colors = [0] * (n)
        used = [False] * (n)
        c = 1

        order.reverse()
        for v in order:
            if not used[v]:
                dfs2(v, c)
                c += 1
        return (colors)

    def find_solution(colors):
        ans = []
        for i in range(0, 2 * n, 2):
            if colors[i] < colors[i + 1]:
                ans.append(0)
            else:
                ans.append(1)
        return (ans)

    for line in stdin:
        n, m = [int(_) for _ in line.strip(' ').split()]
        statements = [[] for _ in range(m)]
        for i in range(m):
            a, b, c, d = map(int, input().split())
            statements[i].extend([a, b, c, d])
        adj, rev_adj = make_graph(n, m, statements)

        print(adj, rev_adj)

        colors = find_scc(adj, rev_adj, 2 * n)
        ans = find_solution(colors)
        for i in range(n):
            print(ans[i], end="")
        print("\n")


if __name__ == "__main__":
    # sys.setrecursionlimit(1000000)
    # threading.stack_size(2**23)
    # thread = threading.Thread(target=main)
    # thread.start()
    main()
