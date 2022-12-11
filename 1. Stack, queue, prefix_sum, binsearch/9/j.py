import sys
from heapq import *

def main():
	input = sys.stdin.readline
	print = lambda x: sys.stdout.write(str(x) + '\n')
	
	N, K = map(int, input().split())
	M = int(input())
	c = [0] * M
	deleted = [False] * M
	events = []
	for i in range(M):
		c[i], l, r = map(int, input().split())
		c[i] -= 1
		events.append((l, i, 0))
		events.append((r + 1, i, 1))
	events.sort()

	s = []
	ans = [0] * K
	for i, e in enumerate(events):
		while s and deleted[-s[0]]: # delayed deletions
			heappop(s)

		if s:
			assert i > 0
			ans[c[-s[0]]] += e[0] - events[i - 1][0]

		if e[2] == 0: # segment started
			heappush(s, -e[1]) # max-heap
		else:
			deleted[e[1]] = True

	print(" ".join(map(str, ans)))

main()
