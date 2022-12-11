total, n = list(map(int, input().split()))
weights = list(map(int, input().split()))
print(total, n)

d_p = [0] * total
d_c = [0] * total
for i in range(len(weights)):
    for j in range(total):
        if (j + 1) - weights[i] < 0:
            d_c[j] = d_p[j]
        elif d_p[j - weights[i]] > 0:
            d_c[j] = j + 1
        elif weights[i] == j + 1:
            d_c[j] = j + 1
        else:
            d_c[j] = d_p[j]
    d_p = d_c
    d_c = [0] * total

print(max(d_p))
