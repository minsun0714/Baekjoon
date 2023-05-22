from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
A = list(map(int, s.readline().split()))
m = int(s.readline().strip())
B = list(map(int, s.readline().split()))

A.sort()


def binary_search(target, A, start, end):
    while start <= end:
        mid = (start + end) // 2

        if A[mid] == target:
            return 1

        elif target > A[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return 0


for b in B:
    print(binary_search(b, A, 0, n - 1))
