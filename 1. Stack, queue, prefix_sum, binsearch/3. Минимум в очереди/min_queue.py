tokens = ['+ 1', '+ 2', '+ 3', '+ 4', '+ 5', '-', '-', '-', '-', '-']
# print(f'str: {str}\nstl: {stl}\n\n')

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
                    n = str.pop()
                    strm.pop()
                    stl.append(n)
                    stlm.append(min(n, stlm[-1]))
                else:
                    strm.pop()
                    n = str.pop()
                    stl.append(n)
                    stlm.append(n)
            stl.pop()
            stlm.pop()
        if stlm:
            print(stlm[-1])
        else:
            print(-1)
    # print('str', str)
    # print('stl', stl)
    # print('strm', strm)
    # print('stlm', stlm)
    # print('\n\n')
