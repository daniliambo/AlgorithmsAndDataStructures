s1 = list()
s2 = list()
import sys

tokens = sys.stdin.read().splitlines()[1:]


# 2 stacks

# Нахождение минимума
def find_min():
    minima = -1
    if len(s1) == 0 and len(s2) != 0:
        minima = s2[-1][1]
    elif len(s1) != 0 and len(s2) == 0:
        minima = s1[-1][1]
    elif len(s1) != 0 and len(s2) != 0:
        minima = min(s2[-1][1], s1[-1][1])
    return minima


# Добавление элемента
def add_el(token):
    minima = token if len(s1) == 0 else min(token, s1[-1][1])
    s1.append((token, minima))
    return find_min()


# Извлечение элемента
def extract_el():
    if not s1 and not s2:
        return -1
    elif len(s2) == 0:
        while s1:
            element = s1[-1][0]
            s1.pop()
            minima = element if len(s2) == 0 else min(element, s2[-1][1])
            s2.append((element, minima))
    s2.pop()
    return find_min()


for t in tokens:
    if t.startswith('+'):
        token = int(t[2:])
        print(add_el(token))
    else:
        print(extract_el())
