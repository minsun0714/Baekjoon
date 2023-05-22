from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

distance = list(map(int, s.readline().split()))
cities = list(map(int, s.readline().split()))
price = 1e9
result = 0

for i in range(n - 1):
    if price > cities[i]:
        price = cities[i]
    result += price * distance[i]

print(result)
