from sys import stdin as s
from collections import deque
import copy

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
board = [list((s.readline().strip())) for _ in range(n)]


def dfs(x, y):
    q = deque([(x, y)])
    copied_board = copy.deepcopy(board)
    copied_board[x][y] = 0
    max_value = 0

    while q:
        x, y = q.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if copied_board[nx][ny] == "L":
                copied_board[nx][ny] = copied_board[x][y] + 1
                q.append((nx, ny))
                max_value = max(max_value, copied_board[nx][ny])

    return max_value


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "W":
            continue
        result = dfs(i, j)
        answer = max(answer, result)

print(answer)
