# необходимо найти количество стоков
from kosaraju import main
from data_input import data_input

V, E, G, G_inv, edges = data_input()

cid = [-1] * (V + 1)
no = 0

colors, c = main(V, G, G_inv)


# if компонентна связности не смотрит никуда, кроме себя, то это и есть сток

# запустить dfs от каждой ксс, если все они компоненты из 1 ксс, то это сток

# get indices of a first appearance with element

def get_ans(c):
    print(G, 'G')
    print(colors, 'colors')

    marked_ccs = [1] * c
    print(marked_ccs)

    for i in G:
        for j in G[i]:
            if colors[i] != colors[j]:
                print(colors[i])
                marked_ccs[colors[i]] = 0

    print(marked_ccs)  # наши стоки, как ксс.
    # Выбрать в них по 1 вершине

    # get indices that are non-0
    ccs = list()
    for i, c in enumerate(marked_ccs):
        if c == 1:
            ccs.append(i)
    print(ccs)

    ans = list()
    for i, c in enumerate(colors):
        if c in ccs:
            ccs.remove(c)
            ans.append(i)
    print('ans')
    print(ans)


get_ans(c)
