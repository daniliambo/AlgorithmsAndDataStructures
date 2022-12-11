import sys
from solve_sat import solve_sat


def process_tests():
    content = sys.stdin.read().splitlines()
    l = len(content)
    i = 0
    while i < l:
        test = list()
        n, m = list(map(int, content[i].split()))
        while m > 0:
            i += 1
            x = list(map(int, content[i].split()))
            x[0] += 1
            x[2] += 1
            test.append(x)
            m -= 1
        i += 1
        solve_sat(n, test)
