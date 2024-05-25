from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
r, c, n = map(int, s.readline().split())
board = [list(map(str, s.readline().strip())) for _ in range(r)]


def check_time(t):
    if t == n:
        for row in board:
            print(''.join(row))
        global flag
        flag = False


def make_next_board(board):
    global t
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                stack.append((i, j))
            else:
                board[i][j] = 'O'
    t += 1
    check_time(t)

    while stack:
        x, y = stack.pop()
        board[x][y] = '.'

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            board[nx][ny] = '.'
    t += 1
    check_time(t)

    return board


if n <= 1:
    for row in board:
        print(''.join(row))
else:
    t = 1
    flag = True
    while flag:
        make_next_board(board)
