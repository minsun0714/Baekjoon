from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
board = [list(s.readline().strip()) for _ in range(n)]


def check_longest(board):
    longest_length = 0

    for row in board:
        count = 0
        for i in range(n):
            if row[i] == row[i - 1]:
                count += 1
            else:
                count = 1
            longest_length = max(longest_length, count)

    for j in range(n):
        count = 0
        for i in range(n):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                count = 1
            longest_length = max(longest_length, count)

    return longest_length


def check_4_sides(x, y):
    global answer
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[x][y] != board[nx][ny]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                answer = max(answer, check_longest(board))
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]


answer = 0
for i in range(n):
    for j in range(n):
        check_4_sides(i, j)
print(answer)
