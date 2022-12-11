import sys


class Graph:
    def __init__(self):
        # init
        self.V, self.S, self.F = list(map(int, input().split()))
        self.m = [[int(j) for j in i.split()] for i in sys.stdin.read().splitlines()]
        # print('Vertices: {}, Start: {}, End: {}'.format(self.V, self.S, self.F))
        # print(self.m)

        # init
        self.used = [-1] * self.V
        self.dist = [sys.maxsize] * self.V
        self.dist[self.S - 1] = 0

    def min_distance(self):
        x = -1
        minimal = sys.maxsize
        for v in range(self.V):
            if self.dist[v] < minimal and self.used[v] == -1:
                minimal = self.dist[v]
                x = v
        return x

    def dijkstra(self):
        for _ in range(self.V):
            x = self.min_distance()

            if x == -1:
                continue

            self.used[x] = 1

            # print(x)  # breaks on x = 1 and y = 0
            for y in range(self.V):  # breaks on x = 1 and y = 0
                if self.m[x][y] != -1 and x != y and self.used[y] == -1:  # remove x != y
                    self.dist[y] = min(self.dist[y], self.dist[x] + self.m[x][y])


g = Graph()
g.dijkstra()
if g.dist[g.F - 1] == sys.maxsize:
    print(-1)
else:
    print(g.dist[g.F - 1])
