from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

A, B, C = map(int, s.readline().strip().split())

visited = [[False] * (B + 1) for _ in range(A + 1)]
q = deque([(0, 0)])


def pour(x, y):
    if not visited[x][y]:
        q.append((x, y))
        visited[x][y] = True


def bfs():
    visited[0][0] = True

    answer = []

    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)

        # x -> z
        water = min(x, C - z)
        pour(x - water, y)

        # y -> z
        water = min(y, C - z)
        pour(x, y - water)

        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)

        # z -> x
        water = min(z, A - x)
        pour(x + water, y)

        # z -> y
        water = min(z, B - y)
        pour(x, y + water)

    return sorted(answer)


result = bfs()
for i in result:
    print(i, end=" ")
