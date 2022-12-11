import sys, threading


def graph(a, b):  # Создаем список смежности
    global G
    if a not in G:
        G[a] = {b}
    else:
        G[a].add(b)
    if b not in G:
        G[b] = {a}
    else:
        G[a].add(b)


def main():
    pass


if __name__ == '__main__':
    sys.setrecursionlimit(2 ** 28)
    threading.stack_size(2 ** 28)
    thread = threading.Thread(target=main)
    thread.start()
