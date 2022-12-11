import sys

data = """4 2
1 2
3 4

"""


def data_input():
    V, E = map(int, data.splitlines()[0].split(' '))
    inp = [list(map(int, x.split())) for x in data.splitlines()[1:-1]]
    adj = [[] for _ in range(V + 1)]
    for e in inp:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return V, E, adj
