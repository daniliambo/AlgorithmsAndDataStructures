# неор. граф
# нет цикла

acyc = """3 2
1 2
2 3

"""
# есть цикл
cyc = """3 3
1 2
2 3
3 1

"""

# input adjacency matrix
n = int(input())
adjl = [[] for n in range(n + 1)]
for i in range(1, n + 1):
    l = list(map(int, input().split())).index(1)
    adjl[i].append(l + 1)

# V, E = [3, 3]
# # adj = [[], [2, 3], [1, 3], [1, 2]]  # неор. случай, cyc
# adj = [[], [2], [3], []]  # неор. случай, cyc

par = -1
used = [-1] * (n + 1)
print(used)


def find_cycle(v, par):
    used[v] = 1
    for u in adjl[v]:
        if u == par:  # parent
            continue
        if used[u] == 1:  # backward
            return True
        if find_cycle(u, v):  # forward
            return True
    return False


ans = 0
for v in range(1, (n + 1)):
    if used[v] == -1:
        if find_cycle(v, par):
            print('Cyclic')
            break
else:
    print('Acyclic')
print(used)
