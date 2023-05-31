from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

soldiers = list(map(int, s.readline().split()))
soldiers.reverse()

dp = [1] * n

for i in range(1, n):
    prev_max = 0
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            prev_max = max(dp[j], prev_max)
            dp[i] = prev_max + 1

print(n - max(dp))
