from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    a = dp[i - 1]
    b = dp[i // 2] if i % 2 == 0 else 1e9
    c = dp[i // 3] if i % 3 == 0 else 1e9
    dp[i] = min(a, b, c) + 1

print(dp)
