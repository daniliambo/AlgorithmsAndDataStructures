def count_cc(colors):
    cc = set()

    def count_comps(colors):
        counter = 0
        colors = colors[1:]

        for c in colors:
            if c in cc:
                continue
            else:
                counter += 1
                cc.add(c)
        return counter

    return count_comps(colors)
