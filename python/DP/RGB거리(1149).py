from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
houses = [list(map(int, s.readline().split())) for _ in range(n)]

for i in range(1, n):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[n-1]))
