from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
stairs = [int(s.readline().strip()) for _ in range(n)]

if n < 3:
    print(sum(stairs))
    exit(0)

dp = [0] * n
dp[0] = stairs[0]

for i in range(1, n):
    option1 = dp[i-3] + stairs[i-1]
    option2 = dp[i-2]
    # 마지막 계단을 반드시 밟아야 하기 때문에 현재 계단을 밟지 않는 optiond은 고려하지 않는다.

    dp[i] = max(option1, option2) + stairs[i]

print(dp[n-1])
