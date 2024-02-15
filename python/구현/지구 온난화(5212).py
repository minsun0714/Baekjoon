from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

r, c = map(int, s.readline().split())
board = [list(map(str, s.readline().strip())) for _ in range(r)]


def check_sinked_or_not(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            count += 1
            continue

        if board[nx][ny] == 'X':
            continue

        count += 1

    visited[x][y] = 'X' if count < 3 else '.'


visited = [['.'] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            check_sinked_or_not(i, j)

min_x, max_x = 1e9, 0
min_y, max_y = 1e9, 0

for i in range(r):
    for j in range(c):
        if visited[i][j] == 'X':
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

for row in visited[min_x:max_x + 1]:
    print(''.join(row[min_y:max_y + 1]))
