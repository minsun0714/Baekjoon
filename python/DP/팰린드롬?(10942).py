from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
nums = list(map(int, s.readline().split()))
m = int(s.readline())

dp = [[0] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if i == j or j == i + 1 and nums[i] == nums[j]:
            dp[i][j] = 1
        elif i < n - 1 and nums[i] == nums[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

for _ in range(m):
    a, b = map(int, s.readline().split())
    print(dp[a - 1][b - 1])
