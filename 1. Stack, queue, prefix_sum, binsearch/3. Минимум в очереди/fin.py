import sys

# tokens = ['+ 1', '-', '+ 3', '-', '+ 10', '+ 3', '+ 4', '-', '-', '-']
# tokens = ['+ 1', '+ 2', '+ 3', '+ 4', '+ 5', '-', '-', '-', '-', '-']
# tokens = ['+ 3', '+ 2', '-', '+ 4', '+ 10', '-', '-', '-', '1', '1']

tokens = sys.stdin.read().splitlines()[1:]
stl = list()
str = list()
stlm = list()
strm = list()

for token in tokens:
    if token.startswith('+'):
        n = int(token[2:])
        if str:
            str.append(n)
            strm.append(min(n, strm[-1]))
        else:
            str.append(n)
            strm.append(n)
        if stlm:
            print(min(strm[-1], stlm[-1]))
        else:
            print(strm[-1])
    else:
        if stl:
            stl.pop()
            stlm.pop()
        else:
            while str:
                if stl:
                    strm.pop()
                    n = str.pop()
                    stl.append(n)
                    stlm.append(min(n, stlm[-1]))
                else:
                    strm.pop()
                    n = str.pop()
                    stl.append(n)
                    stlm.append(n)
            stl.pop()
            stlm.pop()
        if stlm and strm:
            print(min(stlm[-1], strm[-1]))
        elif stlm:
            print(stlm[-1])
        else:
            print(-1)
