from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

nums = list(map(int, s.readline().split()))

dp = [0] * n

for i in (range(0, n)):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))
