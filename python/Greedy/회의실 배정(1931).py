from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

schedule = []
for i in range(n):
    schedule.append(list(map(int, s.readline().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for start_i, end_i in schedule:
    if end == 0 or start_i >= end:
        count += 1
        end = end_i

print(count)
