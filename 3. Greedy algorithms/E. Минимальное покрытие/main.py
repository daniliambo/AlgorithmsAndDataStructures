import sys

m = int(input())
segs_all = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]
segs_all.pop()

segs_all.sort(key=lambda x: (x[0], x[1]))

border = 0
ans = list()
cur_segs = list()

while border < m:
    counter = 0
    cur_segs = list()
    for i in range(len(segs_all)):
        if segs_all[i][0] <= border:
            cur_segs.append(segs_all[i])
            counter += 1
        else:
            break
    if len(cur_segs) == 0:
        print('No solution')
        break
    cur_segs.sort(key=lambda x: x[1])
    ans.append(cur_segs[-1])
    border = cur_segs[-1][1]
    segs_all = segs_all[counter:]
else:
    print(len(ans))
    for x in ans:
        print(' '.join([str(n) for n in x]), end='\n')
