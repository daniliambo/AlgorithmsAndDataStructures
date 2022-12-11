n = 10
arr = [(0, 0, 0)] * (n + 1)

for i in range(1, len(arr)):
    cur = []
    if i % 3 == 0:
        print(i // 3)
        cur.append(arr[i // 3])
    if i % 2 == 0:
        cur.append(arr[i // 2])
    cur.append(arr[i - 1])
    cur.sort()
    arr[i] = (cur[0][0] + 1, cur[0][2], i)
ans = []
element = arr[len(arr) - 1]
while element[2] != 0:
    ans.append(str(element[2]))
    element = arr[element[1]]
ans.reverse()

print('------------------------')
print(len(ans) - 1)
print(*ans)
