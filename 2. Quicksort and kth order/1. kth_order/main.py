import itertools


def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8


def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen)
        d = next(gen)
        yield (c << 8) ^ d


def kth_quicksort(arr, l, r, k):
    pivot = partition(arr, l, r)
    if (pivot - l == k - 1):
        return arr[pivot]
    if (pivot - l > k - 1):
        return kth_quicksort(arr, l, pivot - 1, k)
    else:
        return kth_quicksort(arr, pivot + 1, r, k - pivot + l - 1)


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


n, k = map(int, input().split())
a, b = map(int, input().split())
arr = list(itertools.islice(nextRand32(a, b), n))

print(kth_quicksort(arr, 0, n - 1, k))
