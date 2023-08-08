from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

schedule = []
for _ in range(n):
    schedule.append(list(map(int, s.readline().split())))

dp = [0] * 21

for i in range(n, 0, -1):
    t, p = schedule[i - 1]
    rest_days = n + 1 - i
    if rest_days < t:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(p + dp[i + t], dp[i + 1])

print(dp[1])
