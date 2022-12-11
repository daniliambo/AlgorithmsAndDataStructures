import itertools


def nextRand24(a, b, m):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield (cur >> 8) % m


# n, m = map(int, input().split())
# a, b = map(int, input().split())
n, m = [5, 5]
a, b = [19, 18]

arr = list(itertools.islice(nextRand24(a, b, m), n))


def merge_sort(arr, l, r):
    if l >= r:
        return 0
    middle = (l + r) // 2
    sum_l = merge_sort(arr, l, middle)
    sum_r = merge_sort(arr, middle + 1, r)
    sum_t = merge(arr, l, r, middle)

    return sum_l + sum_r + sum_t


def merge(arr, l, r, middle):
    l_arr = arr[l:middle + 1]
    r_arr = arr[middle + 1:r + 1]
    i = 0
    j = 0
    k = l
    sum_t = 0

    while (i < len(l_arr)) and (j < len(r_arr)):
        if (l_arr[i] > r_arr[j]):
            arr[k] = r_arr[j]
            j += 1
            k += 1
            sum_t += len(l_arr) - i
        else:
            arr[k] = l_arr[i]
            i += 1
            k += 1

    while len(l_arr) > i:
        arr[k] = l_arr[i]
        k += 1
        i += 1

    while len(r_arr) > j:
        arr[k] = r_arr[j]
        k += 1
        j += 1
    return sum_t


arr = [1, 4, 2, 8]
print(arr)
# считать для каждого элемента количество перестановок
l = 0
r = len(arr)
print(merge_sort(arr, l, r))
