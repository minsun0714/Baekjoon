from sys import stdin as s
from bisect import bisect_left, bisect_right

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
cards = sorted(list(map(int, s.readline().split())))
m = int(s.readline())
nums = list(map(int, s.readline().split()))
for num in nums:
    print(bisect_right(cards, num) - bisect_left(cards, num), end=" ")
