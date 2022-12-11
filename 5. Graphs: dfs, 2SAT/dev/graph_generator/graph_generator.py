from random import randint

with open('test.txt', 'w') as f:
    vertex = set()
    edges = set()
    for _ in range(10 ** 5):
        a, b = randint(1, 10 ** 5), randint(1, 10 ** 5)
        vertex.add(a)
        vertex.add(b)
        edges.add((a, b))
    print(max(vertex), min(vertex))
    f.write(str(100001) + ' ' + str(len(edges)) + '\n')
    for elem in edges:
        f.write(str(elem[0]) + ' ' + str(elem[1]) + '\n')
