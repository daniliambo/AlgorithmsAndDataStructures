import sys

infty = sys.maxsize
input_str = input()
n = len(input_str)
dp = [[infty] * (n + 1) for i in range(n + 1)]
sol_dp = [[-1] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    dp[i][i] = 1

for i in range(n - 1):
    if (input_str[i] == '(' and input_str[i + 1] == ')') or (input_str[i] == '[' and input_str[i + 1] == ']') \
            or (input_str[i] == '{' and input_str[i + 1] == '}'):
        dp[i][i + 1] = 0

for i in range(2, n + 1):
    for left in range(n - i + 1):
        right = left + i - 1
        if (input_str[left] == '(' and input_str[right] == ')') or (input_str[left] == '[' and input_str[right] == ']') \
                or (input_str[left] == '{' and input_str[right] == '}'):
            dp[left][right] = min(dp[left][right], dp[left + 1][right - 1])
        for mid in range(left, right):
            current = dp[left][mid] + dp[mid + 1][right]
            if dp[left][right] > current:
                dp[left][right] = current
                sol_dp[left][right] = mid

print(n - dp[0][n - 1])
