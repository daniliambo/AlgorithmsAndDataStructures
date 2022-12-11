from modules import input_data_2
from modules import find_cc
from modules import count_cc


def main():
    V, E, adj = input_data_2.data_input()
    colors = find_cc.find_cc(V, adj)
    print(count_cc.count_cc(colors))
    print(*colors[1:])


if __name__ == '__main__':
    main()
