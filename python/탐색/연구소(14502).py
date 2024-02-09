from sys import stdin as s
import copy

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def spread_virus(x, y, copied_board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if copied_board[nx][ny]:
                continue

            copied_board[nx][ny] = 2
            stack.append((nx, ny))

    return copied_board


ans = 0


def make_walls(depth, start_n, start_m):
    if depth == 3:
        copied_board = copy.deepcopy(board)
        for i in range(n):
            for j in range(m):
                if copied_board[i][j] == 2:
                    spread_virus(i, j, copied_board)
        count_safe_area = sum([row.count(0) for row in copied_board])
        global ans
        ans = max(ans, count_safe_area)

        return

    for i in range(start_n, n):
        for j in range(start_m, m):
            if board[i][j] == 0:
                board[i][j] = 1
                make_walls(depth + 1, i, j)
                board[i][j] = 0

        start_m = 0


make_walls(0, 0, 0)
print(ans)
