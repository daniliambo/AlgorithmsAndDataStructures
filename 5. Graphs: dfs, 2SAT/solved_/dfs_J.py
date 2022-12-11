
import sys
import threading

def euler(v, g, ans, seen):
    while len(g[v]) > 0:
        u = g[v].pop()
        g[u].remove(v)
        euler(u, g, ans, seen)
        ans.append((u, v))

def main():
    global n
    n, m = map(int, input().split())
    g = [set() for _ in range(n+1)]
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)
        edges.add((u, v))
        edges.add((v, u))

    for i in range(len(g)):
        if len(g[i]) % 2 != 0:
            g[0].add(i)
            g[i].add(0)

    ans = []
    seen = set()
    euler(1, g, ans, seen)
    paths = []
    i = 0
    while i < len(ans):
        new_p = []
        while i != len(ans) and ans[i][0] != 0 and ans[i][1] !=0:
            if len(new_p) == 0:
                new_p.append(ans[i][0])
            new_p.append(ans[i][1])
            i += 1
        else:
            if i == len(ans) and len(paths) > 0:
                paths[0] = new_p + paths[0][1:]
            else:
                if len(new_p) > 0:
                    paths.append(new_p)
        i += 1
    print(len(paths))
    for p in paths:
        print(*p)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()