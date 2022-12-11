# input
V, E = map(int, input().split())
# print(V, E)

# init G
G = {}
for i in range(1, V + 1):
    G[i] = set()

# fill G
i = 0
while i < E:
    x = list(map(int, input().split()))
    G[x[0]].add((x[1], x[2]))
    i += 1
# print(G)

# init
# start = 1, fin = V

dp = [float('-inf')] * (V + 1)
dp[1] = 0

for d in range(V):  # V – default
    x = -1
    for v in range(1, V + 1):
        for u, w in G[v]:
            dp_ = dp[u]
            dp[u] = max(dp[u], dp[v] + w)
            if dp_ != dp[u]:
                x = 1
    if d == V - 2:
        dp_1 = dp[:]

if dp[V] == float('-inf'):
    print(':(')
else:
    if dp == dp_1:
        print(dp[V])
    else:
        print(':)')
    # если увеличилось, то :)
    # иначе – :( + вывести наибольшее число

# all values are incremented if dp > dp_1
# if negative cycle – nothing happens
