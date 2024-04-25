from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m, r = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]

while r:
    r -= 1
    row_size, col_size = n, m

    s = 0

    while s < min(row_size, col_size):
        temp = board[s][s]

        for i in range(s, col_size - 1):
            board[s][i] = board[s][i + 1]

        for i in range(s, row_size - 1):
            board[i][col_size - 1] = board[i + 1][col_size - 1]

        for i in range(col_size - 1, s-1, -1):
            board[row_size - 1][i] = board[row_size - 1][i - 1]

        for i in range(row_size - 1, s, -1):
            board[i][s] = board[i - 1][s]

        board[s + 1][s] = temp

        s += 1
        row_size -= 1
        col_size -= 1

for row in board:
    print(*row)
