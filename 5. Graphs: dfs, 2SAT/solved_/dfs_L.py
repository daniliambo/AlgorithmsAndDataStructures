import sys
import threading

def euler(v, g, ans):
    while len(g[v]) > 0:
        u = g[v].pop()
        euler(u, g, ans)
        ans.append((v, u))

def main():
    n = int(input())
    substrs = []
    for i in range(n):
        s = input()
        substrs.append(s)
    g = {}
    in_deg = {}
    out_deg = {}
    for i in range(n):
        pref, suf = substrs[i][:-1], substrs[i][1:]
        g[pref] = g.get(pref, [])
        g[suf] = g.get(suf, [])
        g[pref].append(suf)
        out_deg[pref] = out_deg.get(pref, 0) + 1
        in_deg[suf] = in_deg.get(suf, 0) + 1
    cnt_start = 0
    cnt_end = 0
    is_euler = True
    start = substrs[0][:-1]
    for node in g:
        in_deg[node] = in_deg.get(node, 0)
        out_deg[node] = out_deg.get(node, 0)
        if abs(in_deg[node] - out_deg[node]) > 1:
            is_euler = False
            break
        elif in_deg[node] - out_deg[node] == 1:
            cnt_end += 1
        elif out_deg[node] - in_deg[node] == 1:
            cnt_start += 1
            start = node
        if cnt_end > 1 or cnt_start > 1:
            is_euler = False
            break
    if not is_euler or cnt_start != cnt_end:
        print("NO")
    else:
        ans = []
        euler(start, g, ans)
        ans.reverse()
        code = []
        for i in range(len(ans)):
            if len(code) == 0:
                code.append(ans[i][0])
            code.append(ans[i][1][-1])
        code = ''.join(code)
        if len(code) < n + 2:
            print("NO")
        else:
            print("YES")
            print(code)

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()