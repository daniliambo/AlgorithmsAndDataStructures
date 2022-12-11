# num = 10
num = 962340
a = [0] * (num + 1)  # для каждого числа пока заполняем по 0 операций
a[1] = 0  # продублирую для наглядности чтобы получить 1 нужно 0 операций
for n in range(2, num + 1):  # для каждого числа из диапазона
    minimal = a[n - 1] + 1  # смотрим сколько потребовалось операций для предыдущего и прибавляем
    if n % 2 == 0:
        minimal = min(minimal, a[n // 2] + 1)  # сравниваем сколько операций потребовалось для n//2+1
    if n % 3 == 0:
        minimal = min(minimal, a[n // 3] + 1)  # аналогично
    a[n] = minimal  # заполняем вместо 0 количество операций

operations = []
i = num
while i > 1:
    if i % 3 == 0 and a[i] == a[i // 3] + 1:
        operations.insert(0, 3)
        i //= 3
        continue
    if i % 2 == 0 and a[i] == a[i // 2] + 1:
        operations.insert(0, 2)
        i //= 2
        continue
    if a[i] == (a[i - 1] + 1):
        operations.insert(0, 1)
        i -= 1
        continue

print(a[num])  # минимальное количество операций для num
print(*operations)  # примененные операции


def calculate(operations):
    sum_ = 1

    for n in operations:
        if n == 1:
            sum_ += n
        else:
            sum_ *= n
    print(sum_)


calculate(operations)
