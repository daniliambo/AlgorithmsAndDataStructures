tokens = ['+ 1', '-', '+ 3', '-', '+ 10', '+ 3', '+ 4', '-', '-', '-']
stack = list()
min_stack = list()

# for token in tokens:
#     if token.startswith('+'):
#         num = int(token[2:])
#         if stack:
#             stack.append(num)
#             min_stack.append(min(num, min_stack[-1]))
#         else:
#             stack.append(num)
#             min_stack.append(num)
#         print(min_stack[-1])
#     else:
#         stack.pop()
#         min_stack.pop()
#         if min_stack:
#             print(min_stack[-1])
#         else:
#             print(-1)

# 1 stack realization
# (1, 2)

for token in tokens:
    if token.startswith('+'):
        num = int(token[2:])
        if stack:
            stack.append((num, min(num, stack[-1][1])))
        else:
            stack.append((num, num))
        print(stack[-1][1])
    else:
        stack.pop()
        if stack:
            print(stack[-1][1])
        else:
            print(-1)
