from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

t = int(s.readline())

for _ in range(t):
    count_0, count_1 = 0, 0
    n = int(s.readline())

    if n == 0:
        print(1, 0)
        continue

    dp = [(0, 0)] * (n + 1)
    dp[0] = (1, 0)
    dp[1] = (0, 1)

    for i in range(2, n + 1):
        (a, b) = dp[i - 1]
        (c, d) = dp[i - 2]

        dp[i] = (a + c, b + d)

    (x, y) = dp[n]
    print(x, y)
