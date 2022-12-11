from time import process_time


# print('\n'.join([' '.join([str(d[i][j]) for j in range(la2 + 1)]) for i in range(la1 + 1)]))
# In scientific notation, the letter E is used to mean "10 to the power of."
# For example, 1.314E+1 means 1.314 * 101 which is 13.14 .

def editdistBU(a1, a2):
    t1 = process_time()
    la1 = len(a1)
    la2 = len(a2)
    d = [[0 for x in range(len(a1) + 1)] for x in range(len(a2) + 1)]
    for i in range(len(a1) + 1):
        d[i][0] = i
    for j in range(len(a2) + 1):
        d[0][j] = j
    for i in range(1, len(a1) + 1):
        for j in range(1, len(a2) + 1):
            c = 0 if a1[i - 1] == a2[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c)
    t2 = process_time()
    return (d[la1][la2], t2 - t1)


# str1 = 'jkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhd'
# str2 = 'jkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhdjkhdfgokdsjbvihwebvuhbouhefbvnodkjsnvljklfkdkjghdfjkghdkjfghdkjfhgdkjfhgdkjfhd'
str1 = 'abc'
str2 = 'bca'

print(editdistBU(str1, str2))
