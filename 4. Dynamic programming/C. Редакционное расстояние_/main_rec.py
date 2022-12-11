import time


# расстояние редактирования / расстояние Левенштейна
# вставка, удаление, замена символов: редакторская вставка


def init(a, b):
    a = [*a]
    b = [*b]
    n = len(a) + 1
    m = len(b) + 1
    d = [[-1 for _ in range(m)] for _ in range(n)]

    return a, b, n, m, d


def compare(i, j):
    if a[i] == b[j]:
        return 0
    else:
        return 1


def ed(i, j):
    print(1)
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
    t1 = time.process_time()
    for i in range(1, n):
        for j in range(1, m):
            ed(i, j)
    t2 = time.process_time()
    return (d[n - 1][m - 1], t2 - t1)


if __name__ == '__main__':
    str1 = 'jkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhd'
    str2 = 'jkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhd'
    a, b, n, m, d = init(str1, str2)
    print(main())
