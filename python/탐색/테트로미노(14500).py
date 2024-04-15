from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def get_poliomino(x, y):
    global answer
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y, [(x, y)], board[x][y])])

    while q:
        x, y, selected, score = q.popleft()

        if len(selected) == 3:
            [(a, b), (c, d), (e, f)] = selected
            temp = 0
            if a == c and c == e:
                if c > 0:
                    temp = board[c - 1][d]
                if c < n - 1:
                    temp = max(temp, board[c + 1][d])
            if b == d and d == f:
                if d > 0:
                    temp = max(temp, board[c][d - 1])
                if d < m - 1:
                    temp = max(temp, board[c][d + 1])
            answer = max(answer, score + temp)

        if len(selected) == 4:
            answer = max(answer, score)
        if len(selected) == 5:
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if (nx, ny) in selected:
                continue

            q.append((nx, ny, selected + [(nx, ny)], score + board[nx][ny]))


answer = 0
for i in range(n):
    for j in range(m):
        get_poliomino(i, j)
print(answer)
