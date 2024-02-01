from sys import stdin as s
from collections import deque
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
dict = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, s.readline().split())
    dict[a].append(b)
    dict[b].append(a)

q = deque([1])
visited = [0] * (n + 1)
visited[1] = -1

while q:
    cur = q.popleft()

    for next in dict[cur]:
        if not visited[next]:
            visited[next] = cur
            q.append(next)

for parent in visited[2:]:
    print(parent)
