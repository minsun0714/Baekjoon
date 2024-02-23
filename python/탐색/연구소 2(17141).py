from sys import stdin as s
from collections import deque
import copy

s = open("input.txt", "rt")
n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]

virus_starts = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_starts.append((i, j))
            board[i][j] = 0


def bfs(copied_board, selected):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque(selected)

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if copied_board[nx][ny]:
                continue

            copied_board[nx][ny] = copied_board[x][y] + 1

            q.append((nx, ny))

    for row in copied_board:
        if row.count(0):
            return

    global ans
    max_val = 0
    for k in range(n):
        for l in range(n):
            if copied_board[k][l] > max_val:
                max_val = copied_board[k][l]
    ans = min(ans, max_val)


def dfs(depth, selected, start):
    if depth == m:
        copied_board = copy.deepcopy(board)
        for x, y in selected:
            copied_board[x][y] = 1
        bfs(copied_board, selected)
        return

    for i in range(start, len(virus_starts)):
        dfs(depth + 1, selected + [virus_starts[i]], i + 1)


ans = 1e9
dfs(0, [], 0)
print(ans - 1 if ans != 1e9 else -1)
