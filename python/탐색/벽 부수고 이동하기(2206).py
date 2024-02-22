from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
if n == 1 and m == 1:
    print(1)
    exit(0)

board = [list(map(int, s.readline().strip())) for _ in range(n)]


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0, 0)])

    while q:
        x, y, s = q.popleft()

        for i in range(4):
            nx, ny, ns = x + dx[i], y + dy[i], s

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny][ns]:
                continue

            if board[nx][ny] == 1:
                if ns == 1:
                    continue
                else:
                    ns = 1

            visited[nx][ny][ns] = visited[x][y][s] + 1

            q.append((nx, ny, ns))

            if nx == n - 1 and ny == m - 1:
                print(visited[n - 1][m - 1][ns])
                exit(0)


visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
bfs()
print(-1)
