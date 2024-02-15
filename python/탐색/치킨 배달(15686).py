from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())

city = []
chickens = []
houses = []

for i in range(n):
    row = list(map(int, s.readline().split()))
    city.append(row)
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        if row[j] == 2:
            chickens.append((i, j))


ans = 1e9


def back_tracking(depth, start, chicken_candidates):
    if depth == m:
        chicken_distances = 0
        for hx, hy in houses:
            min_chicken_distance = 1e9
            for cx, cy in chicken_candidates:
                min_chicken_distance = min(
                    min_chicken_distance, abs(cx - hx) + abs(cy - hy))
            chicken_distances += min_chicken_distance
        global ans
        ans = min(ans, chicken_distances)
        return

    for i in range(start, len(chickens)):
        back_tracking(depth + 1, i + 1, chicken_candidates + [chickens[i]])


back_tracking(0, 0, [])
print(ans)
