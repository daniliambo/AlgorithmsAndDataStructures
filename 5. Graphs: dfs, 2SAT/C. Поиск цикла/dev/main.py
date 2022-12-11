# data input
import data_input
from collections import deque


V, E, adjl = data_input.data_input()

# print(V, E, adjl)
V, E = 2, 2
colors = [-1] * (V + 1)
stack = deque()


def find_cycle(v):
    stack.append(v)
    colors[v] = 1
    for u in adjl[v]:
        # stack.append(u)
        if colors[u] == -1:  # tree
            if find_cycle(u):
                return True
        # stack.pop()
        if colors[u] == 1:  # back
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

if stack:
    print(*stack)
