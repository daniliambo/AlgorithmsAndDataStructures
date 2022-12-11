import sys
import threading

def euler(v, g, ans):
    while len(g[v]) > 0:
        u = g[v].pop()
        ans.append((v, u))
        euler(u, g, ans)

def get_sec(d, k):
    if k == 1:
        return [[str(i)] for i in range(d)]
    sec = []
    for subsec in get_sec(d, k-1):
        for j in range(d):
            sec.append(subsec + [str(j)])
    return sec

def debrejn_g(d,k):
    nodes = get_sec(d, k)
    for i in range(len(nodes)):
        nodes[i] = ''.join(nodes[i])
    g = {}
    for i in range(len(nodes)):
        g[nodes[i]] = []
        for j in range(d):
            suff = nodes[i][1:]
            g[nodes[i]].append(suff + str(j))

    return nodes, g


def main():
    d, k = map(int, input().split())
    if k == 1:
        code = [str(i) for i in range(d)]
    else:
        nodes, g = debrejn_g(d, k-1)
        ans = []
        euler(nodes[0], g, ans)
        code = []
        for i in range(len(ans)):
            if len(code) == 0:
                code.append(ans[i][0])
            code.append(ans[i][1][-1])

    print(''.join(code))

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()