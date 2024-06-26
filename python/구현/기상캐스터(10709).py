from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

h, w = map(int, s.readline().split())
board = [list(s.readline().strip()) for _ in range(h)]


for i in range(h):
    for j in range(w):
        if board[i][j] == 'c':
            board[i][j] = 0
        elif board[i][j - 1] != '.' and j:
            board[i][j] = board[i][j - 1] + 1

for i in range(h):
    for j in range(w):
        if board[i][j] == '.':
            board[i][j] = -1
    print(*board[i])
