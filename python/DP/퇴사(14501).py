from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

schedule = []
for i in range(n):
    schedule.append(list(map(int, s.readline().split())))

dp = [0] * 21

for i in range(n, 0, -1):
    rest = n - i + 1
    time_cost = schedule[i - 1][0]

    if rest < time_cost:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + time_cost] + schedule[i - 1][1], dp[i + 1])

print(dp[1])
