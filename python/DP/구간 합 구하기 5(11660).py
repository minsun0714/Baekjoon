from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - \
            dp[i - 1][j - 1] + board[i - 1][j - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, s.readline().split())

    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
