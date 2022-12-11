def fib(n):
    prev = 0
    curr = 1

    for i in range(n - 1):
        curr_ = prev + curr
        curr, prev = curr_, curr
    return curr_


print(fib(7))
