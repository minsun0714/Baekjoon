from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())

board = [list(map(int, s.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs():
    stack = [(0, 0)]
    visited = [[0] * m for _ in range(n)]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                continue
            stack.append((nx, ny))


def melt():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0
                global count
                count += 1


t = 0
prev_count = 0
while True:
    dfs()
    count = 0
    melt()
    if count == 0:
        print(t)
        print(prev_count)
        break
    t += 1
    prev_count = count
