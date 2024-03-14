from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
board = [list(s.readline().strip()) for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            x, y = i, j
            break


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

            if visited[nx][ny]:
                continue

            if board[nx][ny] == 'X':
                continue

            visited[nx][ny] = 1
            if board[nx][ny] == 'P':
                global answer
                answer += 1
            stack.append((nx, ny))


visited = [[0] * m for _ in range(n)]
visited[x][y] = 1
answer = 0
dfs(x, y)
print(answer if answer else 'TT')
