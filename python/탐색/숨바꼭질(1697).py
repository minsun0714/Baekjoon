from sys import stdin as s
from collections import deque

# s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = list(map(int, s.readline().strip().split()))

array = [0 for _ in range(100001)]

q = deque()
q.append(n)

dx = [-1, 1, 2]


def bfs():
    if k <= n:
        return n - k

    while q:
        x = q.popleft()

        for i in range(3):
            nx = x * dx[i] if i == 2 else x + dx[i]

            if nx < 0 or nx > 100000:
                continue
            if array[nx]:
                continue

            array[nx] = array[x] + 1
            q.append(nx)

            if nx == k:
                return array[nx]


print(bfs())
