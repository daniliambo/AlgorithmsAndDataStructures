adjm = """
4
0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0


"""
n = int(input())
adjl = [[] for n in range(n + 1)]
for i in range(1, n + 1):
    l = list(map(int, input().split())).index(1)
    adjl[i].append(l + 1)
