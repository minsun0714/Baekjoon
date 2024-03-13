from sys import stdin as s
from bisect import bisect_left

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
t = int(s.readline())


def binary_search(x):
    return bisect_left(b, x)


for _ in range(t):
    n, m = map(int, s.readline().split())
    a = list(map(int, s.readline().split()))
    b = list(map(int, s.readline().split()))

    b.sort()
    count = 0
    for i in a:
        res = binary_search(i)
        count += res
    print(count)
