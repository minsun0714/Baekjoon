from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

if n == 0:
    print(0)
else:
    dp = [1] * n
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[-1])
