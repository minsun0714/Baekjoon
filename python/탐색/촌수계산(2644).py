from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
u, v = map(int, s.readline().split())
m = int(s.readline())
dict = defaultdict(list)

for _ in range(m):
    x, y = map(int, s.readline().split())
    dict[x].append(y)
    dict[y].append(x)


def dfs(root):
    stack = [root]

    while stack:
        cur = stack.pop()

        for next in dict[cur]:
            if not visited[next]:
                visited[next] = visited[cur] + 1
                stack.append(next)


visited = [0] * (n + 1)
visited[u] = 1
dfs(u)
print(visited[v] - 1)
