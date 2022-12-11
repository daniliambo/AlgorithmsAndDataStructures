def recursive_lol(l):
    for i in range(len(l)):
        if isinstance(l[i], (list)):
            recursive_lol(l[i])
        else:
            l[i] = int(l[i])


def unnest_list(l):
    lol2 = list()
    for i in range(len(l)):
        if isinstance(l[i], list):
            unnest_list(l[i])
        else:
            lol2.append(int(l[i]))
