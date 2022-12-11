# by all sublists
w = 6
weights = [2, 4, 1, 2]
values = [7, 2, 5, 1]
w_ss = list()
v_ss = list()
for i in range(len(weights) + 1):
    for j in range(i):
        w_ss.append(weights[j:i])
for i in range(len(values) + 1):
    for j in range(i):
        v_ss.append(values[j:i])
together = list(zip(w_ss, v_ss, [i for i in range(len(v_ss))]))
max_val = 0
group = -1
for i in range(len(together)):
    print(together[i])
    print(sum(together[i][0]) <= w)
    if sum(together[i][0]) <= w and sum(together[i][1]) > max_val:
        max_val = sum(together[i][1])
        group = together[i][2]
print(max_val, group)
print(together[group])
print(weights, values)
