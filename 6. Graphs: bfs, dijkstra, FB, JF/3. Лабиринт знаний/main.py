# V, E input
V, E = list(map(int, input().split()))
# Init G
G = {}
for i in range(V):
    G[i] = list()

# Fill the G
for i in range(E):
    data_list = list(map(int, input().split()))
    G[data_list[0] - 1].append((data_list[1] - 1, data_list[2]))




# BF
def bf():
    inf_value = float("inf")
    d = [-inf_value] * V
    d[0] = 0
    for _ in range(V):
        x = -1
        for i in G:
            for j in range(len(G[i])):
                if d[i] > -inf_value:
                    if d[G[i][j][0]] < d[i] + G[i][j][1]:
                        d[G[i][j][0]] = d[i] + G[i][j][1]
                        x = G[i][j][0]

    return x, d

used = [False] * V
# Restore answer
x, d = bf()
if d[V - 1] == float("-inf"):
    print(":(")
else:
    if x != -1:
        used[x] = True
        val = [x]
        while val:
            curr_v = val.pop()
            for j in G[curr_v]:
                if not used[j[0]]:
                    val.append(j[0])
                    used[j[0]] = True
        if used[V - 1]:
            print(":)")
        else:
            print(d[V - 1])
    else:
        print(d[V - 1])
