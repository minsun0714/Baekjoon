from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        for l in range(j + 1):
            dp[i][j] += dp[i - 1][l]

print(dp[k][n] % 1000000000)
