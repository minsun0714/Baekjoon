from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
r, c = map(int, s.readline().split())
board = [list(s.readline().strip()) for _ in range(r)]
second = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def fill_water(water_list):
    while water_list:
        x, y = water_list.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if board[nx][ny] == 'D' or board[nx][ny] == 'X':
                continue

            board[nx][ny] = '*'


def make_step(second_list):
    while second_list:
        x, y = second_list.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if board[nx][ny] == '*' or board[nx][ny] == 'X':
                continue

            if board[nx][ny] == 'D':
                print(board[x][y])
                exit()

            board[nx][ny] = board[x][y] + 1


while True:
    second_list = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                board[i][j] = 1

            if board[i][j] == second:
                second_list.append((i, j))
    if not second_list:
        print('KAKTUS')
        break
    make_step(second_list)

    water_list = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                water_list.append((i, j))
    fill_water(water_list)
    second += 1
