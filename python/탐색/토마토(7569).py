from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

m, n, h = map(int, s.readline().split())
board = [[list(map(int, s.readline().split()))
          for _ in range(n)] for _ in range(h)]

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


def bfs():
    q = deque([])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    q.append((i, j, k, 0))
    answer = 0
    while q:
        x, y, z, depth = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue

            if board[nx][ny][nz] != 0:
                continue

            board[nx][ny][nz] = board[x][y][z] + 1

            q.append((nx, ny, nz, depth + 1))
        answer = max(answer, depth)
    return answer


answer = bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                print(-1)
                exit()
print(answer)
