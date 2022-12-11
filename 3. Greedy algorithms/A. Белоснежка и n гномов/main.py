n = int(input())
a_i = list(map(int, input().split()))
b_i = list(map(int, input().split()))
arr = [(a_i[i], b_i[i], i + 1) for i in range(n)]

arr.sort(key=lambda x: x[0] + x[1], reverse=True)

for i in range(len(arr) - 1):
    if min(arr[i][1] - arr[i + 1][0], arr[i + 1][1]) > 0:
        continue
    else:
        print(-1)
        break
else:
    print(' '.join([str(x[2]) for x in arr]))
