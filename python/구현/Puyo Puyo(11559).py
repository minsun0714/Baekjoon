from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
board = [list(map(str, s.readline().strip())) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def has_strike(board):
    def dfs(x, y):
        nonlocal flag

        stack = [(x, y, 1, [(x, y)])]

        while stack:
            x, y, depth, arr = stack.pop()

            if depth == 5:
                return

            if depth == 4:
                flag = True
                for a, b in arr:
                    board[a][b] = '.'

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                    continue

                if board[nx][ny] != board[x][y]:
                    continue

                if (nx, ny) in arr:
                    continue

                stack.append((nx, ny, depth + 1, arr + [(nx, ny)]))

    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                dfs(i, j)
    return flag


def has_T_shape(board):
    def dfs(x, y):
        nonlocal flag

        arr = []

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue

            if board[nx][ny] == board[x][y]:
                arr.append((nx, ny))
        if len(arr) == 3:
            flag = True
            arr += [(x, y)]
            for a, b in arr:
                board[a][b] = '.'

    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                dfs(i, j)
    return flag


def gravity(board):
    for i in range(6):
        col = []
        for j in range(12):
            if board[j][i] != '.':
                col.append(board[j][i])
        for j in range(11, -1, -1):
            if col:
                board[j][i] = col.pop()
            else:
                board[j][i] = '.'


answer = 0
while has_strike(board) or has_T_shape(board):
    answer += 1
    gravity(board)
print(answer)
