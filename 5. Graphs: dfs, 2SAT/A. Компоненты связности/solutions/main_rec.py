import sys, threading


# Transforming to adjacency list
def main():
    def data_input():
        V, E = map(int, input().splitlines()[0].split(' '))
        data = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
        adj = [[] for _ in range(V + 1)]
        for e in data:
            # adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        return V, E, adj

    V, E, adj = data_input()
    # -----------------------

    # Поиск к.с. (кол-во)
    used = [-1] * (V + 1)
    colors = [-1] * (V + 1)
    color = 0
    cc = set([])

    # print(used)

    def dfs(v, color):
        used[v] = 1
        colors[v] = color
        for u in adj[v]:
            if used[u] == -1:
                dfs(u, color)

    for v in range(1, V + 1):
        if used[v] == - 1:
            color += 1
            dfs(v, color)

    print(color)
    print(*colors[1:])


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    threading.stack_size(2 ** 15)
    thread = threading.Thread(target=main)
    thread.start()
