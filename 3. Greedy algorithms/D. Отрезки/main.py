import sys

n = int(input())
segs = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]

segs.sort(key=lambda x: (x[1], -x[0]))
counter = 0
pointer = 0

for seg in segs:
    if seg[0] >= pointer:
        counter += 1
        pointer = seg[1]
else:
    print(counter)
