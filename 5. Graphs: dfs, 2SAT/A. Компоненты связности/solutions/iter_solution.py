from collections import deque


# Класс для представления graphического объекта
class Graph:
    # 1ТП4Т Конструктор
    def __init__(self, edges, n):
        # Список списков для представления списка смежности
        self.adjList = [[] for _ in range(n)]

        # добавляет ребра в неориентированный graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Выполнить итеративную поиск в глубину на Graph, начиная с вершины `v`
def iterativeDFS(graph, v, discovered):
    # создает stack, используемый для выполнения итеративной DFS.
    stack = deque()

    # помещает исходный узел в stack
    stack.append(v)

    # Цикл # до тех пор, пока stack не станет пустым
    while stack:

        # Извлечение вершины из stack
        v = stack.pop()

        # , если вершина уже обнаружена, игнорировать ее
        if discovered[v]:
            continue

        # мы достигнем здесь, если выскочившая вершина `v` еще не обнаружена;
        # печатает `v` и обрабатывает его необнаруженные соседние узлы в stack
        discovered[v] = True
        print(v, end=' ')

        # делаем для каждого ребра (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)


if __name__ == '__main__':

    # Список ребер Graph согласно приведенной выше схеме
    edges = [
        # Обратите внимание, что узел 0 не подключен
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
        # (6, 9) вводит цикл
    ]

    # общее количество узлов в Graph (от 0 до 12)
    n = 13

    # строит graph по заданным ребрам
    graph = Graph(edges, n)

    # для отслеживания обнаружена вершина или нет
    discovered = [False] * n

    # Выполнить итеративный обход DFS от всех необнаруженных узлов к
    # охватывает все связанные компоненты Graph
    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)

    print(discovered)
