from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
m = int(s.readline())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

nodes = [[key, value] for key, value in [
    list(map(int, s.readline().split())) for _ in range(m)]]

for node in nodes:
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

visited[1] = True
queue = deque([1])

while queue:
    cur = queue.popleft()
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = True
            queue.append(node)

true_count = 0
for i in range(2, n + 1):
    if visited[i]:
        true_count += 1
print(true_count)
