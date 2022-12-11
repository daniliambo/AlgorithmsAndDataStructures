from queue import PriorityQueue

n, a_main = list(map(int, input().split()))
plus_pr = []
minus_pr = []

used = [0] * n

q = PriorityQueue()

cur_i = 1
for i in range(n):
    a_friend, b_friend = list(map(int, input().split()))
    if (b_friend >= 0):
        plus_pr.append((cur_i, a_friend, b_friend))
    else:
        minus_pr.append((cur_i, a_friend, b_friend))

    cur_i += 1

minus_pr.sort(key=lambda x: x[1] + x[2])
minus_pr.reverse()

plus_pr.sort(key=lambda x: x[1])
result = []
for i in range(len(plus_pr)):
    if (plus_pr[i][1] <= a_main):
        used[plus_pr[i][0] - 1] = 1
        a_main += plus_pr[i][2]

for i in range(len(minus_pr)):
    if (minus_pr[i][1] <= a_main):
        used[minus_pr[i][0] - 1] = 1
        a_main += minus_pr[i][2]
        q.put((minus_pr[i][2], minus_pr[i][0]))
    elif (not q.empty() and q.queue[0][0] < minus_pr[i][2] and a_main - q.queue[0][0] >= minus_pr[i][1]):
        a_main += minus_pr[i][2] - q.queue[0][0]
        my_el = q.get()
        q.put((minus_pr[i][2], minus_pr[i][0]))
        used[my_el[1] - 1] = 0
        used[minus_pr[i][0] - 1] = 1

result = []
for i in range(len(plus_pr)):
    if (used[plus_pr[i][0] - 1] == 1):
        result.append(str(plus_pr[i][0]))

for i in range(len(minus_pr)):
    if (used[minus_pr[i][0] - 1] == 1):
        result.append(str(minus_pr[i][0]))

print(len(result))
print(" ".join(result))
