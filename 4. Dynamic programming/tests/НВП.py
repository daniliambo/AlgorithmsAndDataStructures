import sys

# a = [4, 6, 1, 3, 5, 7, 0, -1]
# 6
# 3, 29, 5, 5, 28, 6

# a = [3, 29, 5, 5, 28, 6]
n = int(input())
a = list(map(int, input().split()))
n = len(a)
d = [1] * n

# calc
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] <= d[j] + 1:
            d[i] = d[j] + 1

# res
max_res = max(d)
print(a)
print(d)

print(max_res)
max_idx = d.index(max_res)
# print(max_idx)
cur_idx = max_idx - 1
ans = list()
ans.append(a[max_idx])
# print(ans)
while cur_idx >= 0:
    # print(d[max_idx] == d[cur_idx] + 1, d[max_idx], d[cur_idx] + 1)
    # print(a[max_idx] > a[cur_idx])
    if d[max_idx] == d[cur_idx] + 1 and a[max_idx] > a[cur_idx]:
        max_idx = cur_idx
        ans.append(a[max_idx])
    cur_idx -= 1
print(*ans[::-1])
