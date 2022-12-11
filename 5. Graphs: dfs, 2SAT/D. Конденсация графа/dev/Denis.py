import sys
import threading

N, M = map(int, input().split())  # переменные
G = {}
Gt = {}
color = [0 for _ in range(N + 1)]
stack = []


# colort = [0 for _ in range(N + 1)]


def graph(a, b):  # Создаем список смежности
    global G
    global Gt
    if a not in G:
        G[a] = {b}
        if b not in Gt:
            Gt[b] = {a}
        else:
            Gt[b].add(a)
    else:
        G[a].add(b)
        if b not in Gt:
            Gt[b] = {a}
        else:
            Gt[b].add(a)


def dfs1(v):  # Запускаем DFS1
    global color
    global stack
    color[v] = 1
    for u in G[v]:
        if color[u] == 0:
            dfs1(u)
    stack.append(v)


def dfs2(v, c):  # DFS2 для инверт. графа
    global color
    color[v] = c
    for u in Gt[v]:
        if color[u] == 0:
            dfs2(u, c)


def main():  # Главная часть программы
    global color
    c = 0
    # init graph
    for _ in range(M):
        h, t = map(int, input().split())
        graph(h, t)

    # fill unfilled vertices
    for i in range(1, N + 1):
        if i not in G:
            G[i] = {}
        if i not in Gt:
            Gt[i] = {}

    #
    for i in range(1, N + 1):
        if color[i] == 0:
            dfs1(i)

    color = [0 for _ in range(N + 1)]

    print(stack)

    # run through invert ts
    while stack:
        a = stack.pop()
        if not color[a]:
            c += 1
            dfs2(a, c)

    print(color)

    ans = set()

    for i in G:
        for j in G[i]:
            if color[i] != color[j]:
                ans.add((color[i], color[j]))

    print(len(ans))


if __name__ == '__main__':
    sys.setrecursionlimit(150000)
    threading.stack_size(2 ** 23)
    thread = threading.Thread(target=main)
    thread.start()
