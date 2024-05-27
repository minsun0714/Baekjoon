from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, f.readline().split())
board = [list(map(int, f.readline().split())) for _ in range(n)]


def move(clouds):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    new_clouds = []
    for x, y in clouds:
        move_x, move_y = (dx[d - 1] * s), (dy[d - 1] * s)
        nx, ny = (x + move_x) % n, (y + move_y) % n
        new_clouds.append((nx, ny))

    return new_clouds


def rain(board, clouds):
    for x, y in clouds:
        board[x][y] += 1
    return board


def water_copy(board, clouds):
    dx = [-1, 1, -1, 1]
    dy = [-1, 1, 1, -1]
    for x, y in clouds:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if board[nx][ny]:
                board[x][y] += 1
    return board


def make_new_clouds(board, clouds):
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.append((i, j))
    return new_clouds


def water_decrease(board, clouds):
    for i, j in clouds:
        if board[i][j] >= 2:
            board[i][j] -= 2
    return board


clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for _ in range(m):
    d, s = map(int, f.readline().split())

    clouds = move(clouds)
    board = rain(board, clouds)
    board = water_copy(board, clouds)
    clouds = make_new_clouds(board, clouds)
    board = water_decrease(board, clouds)
answer = 0
for row in board:
    answer += sum(row)
print(answer)
