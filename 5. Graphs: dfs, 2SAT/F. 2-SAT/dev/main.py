import sys, threading
from process_tests import process_tests


def main():
    process_tests()


if __name__ == "__main__":
    sys.setrecursionlimit(1500000)
    threading.stack_size(2 ** 23)
    thread = threading.Thread(target=main)
    thread.start()
