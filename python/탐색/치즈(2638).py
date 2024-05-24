from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())

board = [list(map(int, s.readline().split())) for _ in range(n)]


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if board[nx][ny] == 1:
                visited[nx][ny] += 1

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1

            stack.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] > 1:
                board[i][j] = 0
                count += 1
    return count


answer = 0
while True:
    visited = [[0] * m for _ in range(n)]
    count = dfs(0, 0)
    if count == 0:
        break
    answer += 1
print(answer)
