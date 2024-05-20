from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())


def dfs():
    q = deque([(n, 0)])
    visited = [0] * 100001
    max_depth = 1e9
    ways = 0

    while q:
        x, depth = q.popleft()

        if x == k:
            ways += 1
            max_depth = depth

        if depth > max_depth:
            print(visited[k])
            break

        dx = [-1, 1, x]

        for i in range(3):
            nx = x + dx[i]

            if nx < 0 or nx > 100000:
                continue

            if visited[nx] and visited[nx] != depth + 1:
                continue

            visited[nx] = depth + 1

            q.append((nx, depth + 1))
    print(ways)


if k <= n:
    print(n - k)
    print(1)
else:
    dfs()
