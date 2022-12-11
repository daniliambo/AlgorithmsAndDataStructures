import sys


def data_input():
    V, E = map(int, input().splitlines()[0].split(' '))
    data = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
    adj = [[] for _ in range(V + 1)]
    for e in data:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return V, E, adj
