from sys import stdin as s
from collections import deque, defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
asc_dict = defaultdict(list)
desc_dict = defaultdict(list)

for _ in range(m):
    a, b = map(int, s.readline().split())
    asc_dict[a].append(b)
    desc_dict[b].append(a)


def dfs(root, dict):
    stack = [root]

    while stack:
        cur = stack.pop()
        for next in dict[cur]:
            if not visited[next]:
                visited[next] = 1
                stack.append(next)


answer = 0
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    visited[i] = 1
    dfs(i, asc_dict)
    dfs(i, desc_dict)
    if sum(visited) == n:
        answer += 1
print(answer)
