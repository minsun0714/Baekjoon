from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

m, n = map(int, s.readline().split())
tomato_box = [list(map(int, s.readline().split())) for _ in range(n)]

ripe_tomato_index = []

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            ripe_tomato_index.append((i, j))

q = deque(ripe_tomato_index)


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                q.append((nx, ny))

    ans = 0
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 0:
                return -1
            ans = max(ans, tomato_box[i][j])

    return ans - 1


print(bfs())
