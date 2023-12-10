from sys import stdin as s
import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

t = int(s.readline())


def dfs(x, y, board):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if board[x][y] == 0:
        return False

    board[x][y] = 0

    dfs(x-1, y, board)
    dfs(x, y-1, board)
    dfs(x, y+1, board)
    dfs(x+1, y, board)

    return True


for _ in range(t):
    [n, m, k] = list(map(int, s.readline().split(' ')))
    board = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        [x, y] = list(map(int, s.readline().split(' ')))
        board[y][x] = 1

    count = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j, board):
                count += 1

    print(count)
