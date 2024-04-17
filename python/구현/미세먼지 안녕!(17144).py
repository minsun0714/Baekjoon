from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m, t = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def counter_clockwise(board, a, c):
    for i in range(a, -1, -1):
        if board[i][0] == -1:
            continue
        board[i][0] = board[i - 1][0]

    for i in range(m - 1):
        board[0][i] = board[0][i + 1]

    for i in range(a):
        board[i][m - 1] = board[i + 1][m - 1]

    for i in range(m - 1, -1, -1):
        if board[a][i - 1] == -1:
            board[a][i] = 0
            continue
        if board[a][i] == -1:
            continue
        board[a][i] = board[a][i - 1]


def clockwise(board, b, c):
    for i in range(b, n - 1):
        if board[i][0] == -1:
            continue
        board[i][0] = board[i + 1][0]

    for i in range(m - 1):
        board[n - 1][i] = board[n - 1][i + 1]

    for i in range(n - 1, b, -1):
        board[i][m - 1] = board[i - 1][m - 1]

    for i in range(m - 1, -1, -1):
        if board[b][i - 1] == -1:
            board[b][i] = 0
            continue
        if board[b][i] == -1:
            continue
        board[b][i] = board[b][i - 1]


while t:
    t -= 1
    stack = []
    purifiers = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                purifiers.append((i, j))
            board[i][j] = [board[i][j], 0]
            if board[i][j][0] > 0:
                stack.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()
        count = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if board[nx][ny][0] == -1:
                continue

            board[nx][ny][1] += board[x][y][0] // 5
            count += 1

        board[x][y][0] -= (board[x][y][0] // 5) * count

    for i in range(n):
        for j in range(m):
            board[i][j] = sum(board[i][j])

    (a, c), (b, c) = purifiers
    counter_clockwise(board, a, c)
    clockwise(board, b, c)

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
