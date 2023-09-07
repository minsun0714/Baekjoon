from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())
heights = list(map(int, s.readline().split()))

interval = []
for i in range(1, n):
    interval.append(heights[i] - heights[i - 1])
interval.sort()

for _ in range(k - 1):
    interval.pop()

print(sum(interval))
