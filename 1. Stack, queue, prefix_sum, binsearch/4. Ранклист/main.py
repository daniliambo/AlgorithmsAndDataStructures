import sys

tokens = sys.stdin.read().splitlines()

l = list()
for i in range(len(tokens)):
    l.append(tokens[i].split(' '))

pos = int(l.pop(0)[1])

sorted_l = sorted(l, key=lambda x: (int(x[0]), -int(x[1])), reverse=True)
counter = 0
for i in range(len(sorted_l)):
    if sorted_l[i] == sorted_l[pos - 1]:
        counter += 1

print(counter)
