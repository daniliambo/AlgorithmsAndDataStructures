# n, m = 4, 49
# vals = [1, 2, 10, 50]

# 4 90
# 1 2 10 50

n, m = list(map(int, input().split()))
vals = list(sorted(map(lambda x: int(x), input().split()), reverse=True))

i = 0
ans = list()
while True:
    if i < len(vals) and m - vals[i] >= 0:
        m -= vals[i]
        ans.append(vals[i])
    elif i <= len(vals):
        i += 1
    else:
        break

print(len(ans))
print(' '.join([str(i) for i in ans]))
