from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
containers = sorted([int(i)
                     for i in s.readline().split()], reverse=True)

m = int(s.readline())
boxes = sorted([int(i) for i in s.readline().split()], reverse=True)

answer = 0

if containers[0] < boxes[0]:
    print(-1)
    exit(0)

while boxes:
    for container in containers:
        for box in boxes:
            if container >= box:
                boxes.remove(box)
                break
    answer += 1

print(answer)
