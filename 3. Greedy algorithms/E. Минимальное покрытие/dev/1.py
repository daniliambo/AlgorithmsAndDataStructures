M = int(input())

main_variables = []
while True:
    L, R = list(map(int, input().split()))
    if L == 0 and R == 0:
        break
    else:
        main_variables.append((L, R))

main_variables.sort(key=lambda x: x[0])

result = []
cur_el = (0, 0)
current_list = []
for i in main_variables:
    if i[0] <= cur_el[1]:
        current_list.append(i)
    elif current_list:
        current_list.sort(key=lambda x: x[1])
        if current_list[-1][1] > cur_el[1]:
            result.append(current_list[-1])
            cur_el = current_list[-1]
            current_list = []
            if cur_el[1] >= M:
                break
            if i[0] <= cur_el[1]:
                current_list.append(i)
        else:
            break
    else:
        break

if current_list:
    current_list.sort(key=lambda x: x[1])
    if current_list[-1][1] > cur_el[1]:
        result.append(current_list[-1])

if not result:
    print("No solution")
elif result[-1][1] < M:
    print("No solution")
else:
    print(len(result))
    for i in result:
        print(str(i[0]) + " " + str(i[1]))
