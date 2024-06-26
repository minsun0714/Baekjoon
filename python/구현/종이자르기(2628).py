from sys import stdin as s
from itertools import product

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
w, h = map(int, s.readline().split())
n = int(s.readline())
verticals = [0, w]
parallels = [0, h]
for _ in range(n):
    is_vertical, x = map(int, s.readline().split())

    if is_vertical:
        verticals.append(x)
    else:
        parallels.append(x)
verticals.sort()
parallels.sort()

for i in reversed(range(len(verticals))):
    verticals[i] -= verticals[i - 1]
for i in reversed(range(len(parallels))):
    parallels[i] -= parallels[i - 1]

prod = [x * y for x, y in list(product(verticals[1:], parallels[1:]))]
print(max(prod))
