from sys import stdin as s
from collections import defaultdict
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())

dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, s.readline().split())
    dict[a].append(b)
    dict[b].append(a)


def bfs(start):
    q = deque([start])

    while q:
        cur = q.popleft()

        for next in dict[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1

    global ans
    ans += 1


visited = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = 1
        bfs(i)

print(ans)
