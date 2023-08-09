from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

distances = list(map(int, s.readline().split()))
prices = list(map(int, s.readline().split()))
prices.pop()

current_price = prices[0]
cost = 0
for i in range(n-1):
    # 더 저렴한 곳이 나오면 갱신
    if prices[i] < current_price:
        current_price = prices[i]

    cost += current_price * distances[i]

print(cost)
