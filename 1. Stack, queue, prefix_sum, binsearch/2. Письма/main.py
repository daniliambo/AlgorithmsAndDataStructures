import sys

# tokens = sys.stdin.read().splitlines()

letter_hostels_n, hostels = map(int, input().split())
rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))

k = 1
i = 0
ans = ''
sum = rooms[1]
sum_prev = rooms[0]
while True:
    if (i < letter_hostels_n[1]) and (letters[i] <= sum):
        print('{} {}\n'.format(k, letters[i] - sum_prev))
        i += 1
    elif k < letter_hostels_n[0]:
        k += 1
        sum_prev = sum
        sum += rooms[k]
    else:
        break
