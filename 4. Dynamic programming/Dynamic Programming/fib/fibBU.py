F = [0 for i in range(50)]
F[1] = 1


def fib(n):
    for x in range(1, n):
        F[x + 1] = F[x] + F[x - 1]




fib(10)
print(F)
