import sys
import threading

def count_dist(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

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
    segments = []
    points = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        segments.append(((x1, y1), (x2, y2)))
        points.append((x1, y1))
        points.append((x2, y2))

    dists = {}
    max_dist = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dst = count_dist(points[i], points[j])
            if dst > max_dist:
                max_dist = dst
            dists[(points[i], points[j])] = dst

    l = 0
    r = max_dist + 1
    m = 0
    while l < r:
        m = (l + r) // 2
        g = {}
        g_rev = {}
        for i in range(n):
            g[(i, 0)] = []
            g[(i, 1)] = []
            g_rev[(i, 0)] = []
            g_rev[(i, 1)] = []
        for i in range(len(segments)):
            for j in range(i+1, len(segments)):
                for k in range(2):
                    if dists[(segments[i][k], segments[j][k])] < m:

                        g[(i, k)].append((j, 1-k))
                        g[(j, k)].append((i, 1-k))
                        g_rev[(i, 1-k)].append((j, k))
                        g_rev[(j, 1-k)].append((i, k))
                    if dists[(segments[i][k], segments[j][1-k])] < m:
                        g[(i, k)].append((j, k))
                        g[(j, 1-k)].append((i, 1-k))
                        g_rev[(i, 1-k)].append((j, 1-k))
                        g_rev[(j, k)].append((i, k))
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

        while i < n:
            if color[(i, 0)] == color[(i, 1)]:
                r = m
                break
            i += 1
        else:

            l = m + 1

    print((l-1) ** 0.5)





if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()