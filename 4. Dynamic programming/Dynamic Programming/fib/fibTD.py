F = [-1 for i in range(6)]


def fib(n):
    if F[n] == -1:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib(n - 1) + fib(n - 2)
    return F[n]


print(fib(5))
