def data_input():
    V, E = list(map(int, input().split()))

    i = V
    data = list()
    while i > 0:
        data.append(list(map(int, input().split())))
        i -= 1

    adjl = [set([]) for _ in range(V + 1)]
    for e in data:
        adjl[e[0]].add(e[1])
    return V, E, adjl


"""
2 2
1 2
1 2


2 2
1 2
2 1



"""