from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
board = [list(map(int, s.readline().split())) for _ in range(19)]


def check(x, y, dx, dy):
    nx, ny = x - dx[1], y - dy[1]
    if 19 > nx >= 0 and 19 > ny >= 0 and board[x][y] == board[nx][ny]:
        return False

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if i == 5:
            if nx >= 19 or ny >= 19:
                return True

            if board[nx][ny] != board[x][y]:
                return True

        if nx >= 19 or ny >= 19:
            return False

        if board[nx][ny] != board[x][y]:
            return False

    return False


same = [0] * 6
prev = [-i for i in range(6)]
next = [i for i in range(6)]

visited = [[0] * 19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        is_winner = False
        if board[i][j]:
            if check(i, j, same, next):
                is_winner = True

            if check(i, j, next, same):
                is_winner = True

            if check(i, j, next, next):
                is_winner = True
            if check(i, j, prev, next):
                is_winner = True
        if is_winner:
            print(board[i][j])
            print(i + 1, j + 1)
            exit()
print(0)
