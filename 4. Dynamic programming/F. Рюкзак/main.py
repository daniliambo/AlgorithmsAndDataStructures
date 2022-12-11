from modules import print_matrix

global weights, dp
# n, s = list(map(int, input().strip().split()))[:2]
# weights = list(map(int, input().strip().split()))[:n]
# values = list(map(int, input().strip().split()))[:n]

n, s = 4, 6
weights = [2, 4, 1, 2]
values = [7, 2, 5, 1]

# calculate dp
dp = [[0] * (s + 1) for i in range(n + 1)]
for i in range(1, n + 1):  # i for item
    for w in range(s + 1):
        dp[i][w] = dp[i - 1][w]
        if w >= weights[i - 1]:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

print_matrix.print_matrix(dp)


# идем на предыдущую строку и смотрим был ли путь, который можно получить, если вычесть из текущего веса наш вес строки.
# если там не 0, а конкретное число

# смотришь на вес предыдущей строки без этой вещи и смотришь стоимость этой штуки и прибавляешь стоимость этой вещи.
# Если в предыдущей строке уже лежит большая стоимость, то мы смогли получить стоимость без этой вещи.

# res
def res(i, j):
    if dp[i][j] == 0:
        return []
    elif dp[i - 1][j] == dp[i][j]:
        result = res(i - 1, j)
    else:
        result = res(i - 1, j - weights[i - 1])
        result.append(str(i))
    return result


result = res(n, s)
print(len(result))
print(" ".join(result))
