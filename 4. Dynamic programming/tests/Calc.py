n = 10
d = [0] * (n + 1)

for i in range(2, n + 1):
    minimal = d[i - 1]
    if i % 2 == 0:
        minimal = min(minimal, d[i // 2])
    if i % 3 == 0:
        minimal = min(minimal, d[i // 3])
    d[i] = minimal + 1
print(d)

ans = list()
while n > 1:
    if d[n - 1] + 1 == d[n]:
        ans.append(1)
        n -= 1
    if d[n // 2] + 1 == d[n] and n % 2 == 0:
        ans.append(2)
        n //= 2
    if d[n // 3] + 1 == d[n] and n % 3 == 0:
        ans.append(3)
        n //= 3
print(ans)
