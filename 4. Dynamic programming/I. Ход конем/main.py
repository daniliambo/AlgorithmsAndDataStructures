n = int(input())

d = {0: [4, 6], 1: [8, 6], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2]}

prev_list = [0] * 10
current_list = [0] * 10

for i in range(10):
    if (i != 0) and (i != 8):
        prev_list[i] = 1

for i in range(1, n):
    for j in range(10):
        if (j != 5):
            ways_arr = d.get(j)
            for way in ways_arr:
                current_list[j] += prev_list[way]
    prev_list = current_list
    current_list = [0] * 10

if (n != 0):
    print(sum(prev_list) % 1000000000)
else:
    print(0)
