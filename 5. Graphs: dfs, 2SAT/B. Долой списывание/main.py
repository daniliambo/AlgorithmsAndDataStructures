import sys


def input_data():
    V, E = list(map(int, input().splitlines()[0].split()))
    data = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
    adj = [[] for _ in range(V + 1)]

    for e in data:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return V, E, adj


def check_bipartition(V, adj):
    colors = [-1] * (V + 1)

    def dfs(v):
        for u in adj[v]:

            if colors[u] == colors[v]:
                return False

            if colors[u] == -1:
                colors[u] = 1 - colors[v]
                if not dfs(u):
                    return False

            if colors[u] != colors[v]:
                pass

        return True

    fail = False

    for v in range(1, V + 1):
        if colors[v] == -1:
            colors[v] = 0
            if not dfs(v):
                fail = True
    return fail


def get_ans(fail):
    if fail == True:
        print('NO')
    else:
        print('YES')


def main():
    V, E, adj = input_data()
    fail = check_bipartition(V, adj)
    get_ans(fail)


if __name__ == '__main__':
    main()
