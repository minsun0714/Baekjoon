from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
arr = [list(map(int, s.readline().split())) for _ in range(n)]
arr.sort()
b = [b for a, b in arr]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if b[i] > b[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
