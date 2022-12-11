# кратные ребра и петли
from kosaraju import main
from data_input import data_input

V, E, G, G_inv, edges = data_input()

counter = 0
count = set()

cid = [-1] * (V + 1)
no = 0

colors, c = main(V, G, G_inv)

# for edge in edges:
#     if colors[edge[0]] == colors[edge[1]]:
#         continue
#     if (colors[edge[0]], colors[edge[1]]) not in count and (colors[edge[0]], colors[edge[1]])[::-1] not in count:
#         count.add((colors[edge[0]], colors[edge[1]]))
#         counter += 1

for i in G:
    for j in G[i]:
        if colors[i] != colors[j]:
            count.add((colors[i], colors[j]))

print(len(count))
