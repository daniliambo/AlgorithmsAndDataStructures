from collections import defaultdict


def bellman_ford(N, graph):
    inf_value = float("inf")
    distances = [-inf_value] * N
    distances[0] = 0
    x = 0
    for i in range(N):
        x = -1  #
        for key in graph:
            for j in range(len(graph[key])):
                if distances[key] > -inf_value:
                    if distances[graph[key][j][0]] < distances[key] + graph[key][j][1]:
                        distances[graph[key][j][0]] = distances[key] + graph[key][j][1]
                        x = graph[key][j][0]

    return x, distances


N, M = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(M):
    data_list = list(map(int, input().split()))
    graph[data_list[0] - 1].append((data_list[1] - 1, data_list[2]))

visited = [False] * N

x, distances = bellman_ford(N, graph)
if distances[N - 1] == float("-inf"):
    print(":(")
else:
    if x != -1:
        visited[x] = True
        check_q = [x]
        while check_q:
            current_v = check_q.pop()
            for j in graph[current_v]:
                if not visited[j[0]]:
                    check_q.append(j[0])
                    visited[j[0]] = True
        if visited[N - 1]:
            print(":)")
        else:
            print(distances[N - 1])
    else:
        print(distances[N - 1])
