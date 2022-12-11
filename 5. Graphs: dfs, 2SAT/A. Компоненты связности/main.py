import sys
from collections import deque


def data_input():
    V, E = map(int, input().splitlines()[0].split(' '))
    data = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
    adj = [[] for _ in range(V + 1)]
    for e in data:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return V, E, adj


def find_cc(V, adj):
    colors = [-1] * (V + 1)
    color = 0

    stack = deque()

    for v in range(1, V + 1):
        if colors[v] == -1:
            color += 1
            stack.clear()
            stack.append(v)
            while stack:
                v = stack.pop()

                if colors[v] != -1:
                    continue

                colors[v] = color

                adjlist = adj[v]

                for i in range(len(adjlist)):
                    u = adjlist[i]
                    if colors[u] == -1:
                        stack.append(u)
    return colors, color


def main():
    V, E, adj = data_input()
    colors, color = find_cc(V, adj)
    print(color)
    print(*colors[1:])


if __name__ == '__main__':
    main()
