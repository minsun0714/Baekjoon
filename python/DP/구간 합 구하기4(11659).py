from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))

dp = [0]
for num in nums:
    dp.append(dp[-1] + num)

for _ in range(m):
    x, y = map(int, s.readline().split())
    ans = dp[y] - dp[x - 1]
    print(ans)
