from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

queue = deque([i for i in range(1, n + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
