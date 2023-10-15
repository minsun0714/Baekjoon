from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())
coin_type = [int(s.readline()) for _ in range(n)]
coin_type = list(set(coin_type))

dp = [10001] * (k + 1)  # 동전을 가장 많이 사용하는 경우 1원으로 10000원을 만들 수 있으므로 10001로 초기화
dp[0] = 0

for i in range(1, k + 1):
    for coin in coin_type:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] < 10001 else -1)
