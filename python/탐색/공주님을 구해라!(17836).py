from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m, t = map(int, s.readline().split())

board = [list(map(int, s.readline().split())) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0, 0)])

while q:
    x, y, s = q.popleft()

    if visited[n - 1][m - 1][0] or visited[n - 1][m - 1][1]:
        time = max(visited[n - 1][m - 1])
        if time - 1 <= t:
            print(time - 1)
        else:
            print('Fail')
        exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if board[nx][ny] == 1 and s == 0:
            continue

        if visited[nx][ny][s]:
            continue

        if board[nx][ny] == 2:
            ns = 1
        else:
            ns = s

        visited[nx][ny][ns] = visited[x][y][s] + 1
        visited[nx][ny][s] = visited[x][y][s] + 1

        q.append((nx, ny, ns))

print('Fail')
