from sys import stdin as s
import itertools

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

board = []

for i in range(n):
    board.append(list(map(str, s.readline().strip())))


def rotate_board(board):
    new_board = []
    for i in range(n):
        row = []
        for j in range(n - 1, -1, -1):
            row.append(board[j][i])
        new_board.append(row)
    return new_board


result = 0


def get_max_candies(board):
    for row in board:
        max_value_each_row = 0
        for _, group in itertools.groupby(row):
            max_value_each_row = max(max_value_each_row, len(list(group)))

        global result
        if max_value_each_row > result:
            result = max_value_each_row


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == board[x][y]:
            continue

        board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
        get_max_candies(board)
        get_max_candies(rotate_board(board))
        board[nx][ny], board[x][y] = board[x][y], board[nx][ny]


for i in range(n):
    for j in range(n):
        solution(i, j)

# print(result)

array = [3, 3, 3, 5, 5, 6, 8, 9, 9, 9, 1, 1, 3, 3, 3, 4, 5]
for key, group in itertools.groupby(array):
    print(key)
    print(list(group))
