from sys import stdin as s
import copy

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split(' '))) for _ in range(n)]
dx = [- 1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melt_ice(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if next_board[nx][ny] == 0:
            continue

        next_board[nx][ny] -= 1


def count_icebergs(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if next_board_copied[nx][ny] == 0:
                continue

            next_board_copied[nx][ny] = 0

            stack.append((nx, ny))

    return True


time = 0
is_more_than_one = False
while True:
    next_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                melt_ice(i, j)

    next_board_copied = copy.deepcopy(next_board)
    count = 0
    for i in range(n):
        for j in range(m):
            if next_board_copied[i][j]:
                if count_icebergs(i, j):
                    count += 1

    board = next_board

    if count == 0:
        break
    time += 1
    if count > 1:
        is_more_than_one = True
        break
print(time if is_more_than_one else 0)
