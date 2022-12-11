# расстояние редактирования / расстояние Левенштейна
# вставка, удаление, замена символов: редакторская вставка


def init():
    # a = 'short'
    # b = 'ports'
    # a = 'ab'
    # b = 'ab'
    a = input()
    b = input()

    a = [*a]
    b = [*b]
    n = len(a) + 1
    m = len(b) + 1
    d = [[-1 for _ in range(m)] for _ in range(n)]

    # print(a, b)
    # dp = [[0] * (m + 1) for i in range(n + 1)]
    # print(d)
    # print('\n'.join([' '.join([str(el) for el in item]) for item in d]))
    return a, b, n, m, d


def compare(i, j):
    if a[i] == b[j]:
        return 0
    else:
        return 1


def ed(i, j):
    if d[i][j] == -1:
        if i == 0:
            d[i][j] = j
        elif j == 0:
            d[i][j] = i
        else:
            insert = ed(i, j - 1) + 1
            delete = ed(i - 1, j) + 1
            sub = ed(i - 1, j - 1) + compare(i - 1, j - 1)
            d[i][j] = min(insert, delete, sub)
    return d[i][j]


def main():
    for i in range(1, n):
        for j in range(1, m):
            ed(i, j)
    # print('\n'.join([' '.join([str(el) for el in item]) for item in d]))
    return d[n - 1][m - 1]


if __name__ == '__main__':
    a, b, n, m, d = init()
    print(main())
