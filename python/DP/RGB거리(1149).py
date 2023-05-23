from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

cost = []

for i in range(n):
    cost.append(list(map(int, s.readline().strip().split())))

for i in range(1, n):
    for j in range(3):
        min_left, min_right = 1e9, 1e9
        left = cost[i - 1][: j]
        right = cost[i - 1][j + 1: n]

        if left:
            min_left = min(left)
        if right:
            min_right = min(right)

        cost[i][j] += min(min_left, min_right)

print(min(cost[n - 1]))
