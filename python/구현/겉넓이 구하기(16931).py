from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]

top, bottom = n * m, n * m

left = 0
for i in range(n):
    for j in range(m):
        if j == 0:
            left += board[i][j]
        elif board[i][j] > board[i][j - 1]:
            left += board[i][j] - board[i][j - 1]

right = 0
for i in range(n):
    for j in reversed(range(m)):
        if j == m - 1:
            right += board[i][j]
        elif board[i][j] > board[i][j + 1]:
            right += board[i][j] - board[i][j + 1]

rotated = []
for j in range(m):
    columns = []
    for i in range(n):
        columns.append(board[i][j])
    rotated.append(columns)

front = 0
for i in range(m):
    for j in range(n):
        if j == 0:
            front += rotated[i][j]
        elif rotated[i][j] > rotated[i][j - 1]:
            front += rotated[i][j] - rotated[i][j - 1]

back = 0
for i in range(m):
    for j in reversed(range(n)):
        if j == n - 1:
            back += rotated[i][j]
        elif rotated[i][j] > rotated[i][j + 1]:
            back += rotated[i][j] - rotated[i][j + 1]
print(front + back + left + right + top + bottom)
