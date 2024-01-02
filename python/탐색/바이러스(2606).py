from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

l = int(s.readline().strip())

graph = [[] for _ in range(n + 1)]

for i in range(l):
    [x, y] = list(map(int, s.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

q = deque([1])
visited = [False] * (n + 1)
visited[1] = True

count = 0

while q:
    cur = q.popleft()

    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            count += 1

print(count)
