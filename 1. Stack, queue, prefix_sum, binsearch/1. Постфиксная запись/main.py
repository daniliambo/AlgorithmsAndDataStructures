import sys
from collections import deque


def main():
    tokens = sys.stdin.read().rstrip().split(' ')

    my_stack = deque()
    for n in tokens:
        if n == '+':
            my_stack.append(int(my_stack.pop()) + int(my_stack.pop()))
        elif n == '*':
            my_stack.append(int(my_stack.pop()) * int(my_stack.pop()))
        elif n == '-':
            r1 = int(my_stack.pop())
            r2 = int(my_stack.pop())
            my_stack.append(r2 - r1)
        else:
            my_stack.append(int(n))
    return my_stack[0]


if __name__ == '__main__':
    print(main())
