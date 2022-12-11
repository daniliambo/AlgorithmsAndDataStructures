import sys
import threading

def dfs(v, g, seen, order):
    seen.add(v)
    for neighbor in g[v]:
        if neighbor not in seen:
            dfs(neighbor, g, seen, order)

    order.append(v)

def dfs2(v, g, color):
    global c
    color[v] = c
    for neighbor in g[v]:
        if neighbor not in color:
            dfs2(neighbor, g, color)


def main():
    global c
    n = int(input())
    wcolor = list(map(int, input().split()))
    connectors = list(map(int, input().split()))
    g = {}
    g_rev = {}
    for i in range(n):
        g[(i, 0)] = []
        g[(i, 1)] = []
        g_rev[(i, 0)] = []
        g_rev[(i, 1)] = []

    options = [[] for _ in range(n)]
    for i in range(len(connectors)):
        options[connectors[i]-1].append(i)
    for i in range(1, len(connectors)):
        if wcolor[connectors[i]-1] == wcolor[connectors[i-1]-1] and connectors[i] != connectors[i-1]:
            if options[connectors[i] - 1][0] == i:
                k1 = 0
            else:
                k1 = 1
            if options[connectors[i-1] - 1][0] == i-1:
                k2 = 0
            else:
                k2 = 1
            g[(connectors[i] - 1, k1)].append((connectors[i-1] - 1, 1 - k2))
            g[(connectors[i-1] - 1, k2)].append((connectors[i] - 1, 1 - k1))
            g_rev[(connectors[i-1] - 1, 1 - k2)].append((connectors[i] - 1, k1))
            g_rev[(connectors[i] - 1, 1-k1)].append((connectors[i-1] - 1, k2))

    if wcolor[connectors[-1]-1] == wcolor[connectors[0]-1] and connectors[-1] != connectors[0]:
        if options[connectors[0] - 1][0] == 0:
            k1 = 0
        else:
            k1 = 1
        if options[connectors[-1] - 1][0] == len(connectors)-1:
            k2 = 0
        else:
            k2 = 1

        g[(connectors[0] - 1, k1)].append((connectors[-1] - 1, 1 - k2))
        g[(connectors[-1] - 1, k2)].append((connectors[0] - 1, 1-k1))
        g_rev[(connectors[-1] - 1, 1 - k2)].append((connectors[0] - 1, k1))
        g_rev[(connectors[0] - 1, 1-k1)].append((connectors[-1] - 1, k2))

    order = []
    seen = set()
    for i in g:
        if i not in seen:
            dfs(i, g, seen, order)

    color = {}
    c = 0
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        if v not in color:
            dfs2(v, g_rev, color)
            c += 1
    i = 0
    ans = []
    while i < len(wcolor):
        if color[(i, 0)] == color[(i, 1)]:
            print('NO')
            break
        elif color[(i, 0)] < color[(i, 1)]:
            ans.append(options[i][1]+1)
        else:
            ans.append(options[i][0]+1)
        i += 1
    else:
        print('YES')
        print(*ans)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()