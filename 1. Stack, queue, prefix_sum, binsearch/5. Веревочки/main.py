import sys

ropes, houses = map(int, input().split())
nums = list(map(int, sys.stdin.read().splitlines()))


def eval(rl):
    counter = 0
    for r in nums:
        ans = r // rl
        counter += ans
    return counter


l, r = 0, (sum(nums) // houses) + 1

while r - l > 1:
    mid = (l + r) // 2
    if eval(mid) >= houses:
        l = mid
    elif eval(mid) < houses:
        r = mid
print(l)
