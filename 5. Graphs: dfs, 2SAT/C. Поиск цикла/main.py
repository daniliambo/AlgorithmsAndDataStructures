# data input
import sys, threading


def main():
    def data_input():
        V, E = list(map(int, input().split()))

        i = E
        data = list()
        while i > 0:
            data.append(list(map(int, input().split())))
            i -= 1

        adjl = [set([]) for _ in range(V + 1)]
        for e in data:
            adjl[e[0]].add(e[1])
        return V, E, adjl

    V, E, adjl = data_input()

    colors = [-1] * (V + 1)
    stack = list()

    def find_cycle(v):
        stack.append(v)
        colors[v] = 1
        for u in adjl[v]:
            if colors[u] == -1:  # tree
                if find_cycle(u):
                    return True
            if colors[u] == 1:  # back
                stack.append(u)
                return True
            if colors[u] == 2:  # cross
                pass
        stack.pop()
        colors[v] = 2
        return False

    for v in range(1, V + 1):
        if colors[v] == -1:
            if find_cycle(v):
                print('YES')
                break
    else:
        print('NO')
    # print(colors)

    if stack:
        item = stack[-1]
        for i in range(len(stack) - 2, -1, -1):
            if stack[i] == item:
                stack = stack[i + 1::]
                print(*stack)
                break


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(2 ** 27)
    thread = threading.Thread(target=main)
    thread.start()
