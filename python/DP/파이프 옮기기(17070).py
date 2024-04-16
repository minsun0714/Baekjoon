from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
board = [list(map(int, s.readline().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if board[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]

        if board[i - 1][j] or board[i][j - 1]:
            continue
        dp[i][j][2] = dp[i - 1][j - 1][0] + \
            dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
print(sum(dp[-1][-1]))
