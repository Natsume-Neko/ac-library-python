# https://atcoder.jp/contests/practice2/tasks/practice2_c

from atcoder.math import floor_sum


def main() -> None:
    import sys

    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, a, b = map(int, sys.stdin.readline().split())
        print(floor_sum(n, m, a, b))


if __name__ == '__main__':
    main()
