from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())

items = []
for _ in range(n):
    items.append(list(map(int, s.readline().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cur_weight, cur_value = items[i - 1]
    for w in range(1, k + 1):
        if w >= cur_weight:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - cur_weight] + cur_value)
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[i][k])
