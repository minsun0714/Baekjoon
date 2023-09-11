from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())
coins = [int(s.readline()) for _ in range(n)]
dp = [0] * (k + 1)

for coin in coins:
    for i in range(coin, k + 1):
        # 새로운 코인만 단독으로 사용하는 경우를 1만큼 추가한다.
        if i == coin:
            dp[i] += 1
        # 그 외에는 새로운 코인을 사용하지 않았던 경우의 수에 새로운 코인을 사용한 경우의 수를 더한다.
        else:
            dp[i] += dp[i - coin]
print(dp[k])
