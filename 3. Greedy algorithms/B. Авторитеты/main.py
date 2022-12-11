import sys
import heapq
import random

n, auth = list(map(int, input().split()))
fr = [list(map(int, x.split()[::-1])) for x in sys.stdin.read().splitlines()]

for i in range(len(fr)):
    fr[i].append(i + 1)

fr.sort(key=lambda x: x[0])

l = 0
for i in range(len(fr)):
    if fr[i][0] >= 0:
        l = i
        break

fr_pos = fr[l:]
fr_neg = fr[:l]
fr_pos.sort(key=lambda x: x[1])
fr_neg.sort(key=lambda x: (x[0] + x[1]), reverse=True)
neg_friends = list()
pos_friends = list()

for friend in fr_pos:
    if auth >= friend[1]:
        auth += friend[0]
        pos_friends.append(friend)
    else:
        break

for friend in fr_neg:
    if auth >= friend[1]:
        auth += friend[0]
        heapq.heappush(neg_friends, friend)
    elif neg_friends and friend[0] >= neg_friends[0][0]:
        auth += friend[0] - neg_friends[0][0]
        heapq.heappop(neg_friends)
        heapq.heappush(neg_friends, friend)
pos_friends.extend(neg_friends)
print(len(pos_friends))
print(' '.join([str(x[2]) for x in pos_friends]))
