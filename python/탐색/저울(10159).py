from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
m = int(s.readline())
descendent_dict = defaultdict(list)
ascendent_dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, s.readline().split())
    descendent_dict[a].append(b)
    ascendent_dict[b].append(a)


def dfs(root, dict):
    stack = [root]

    while stack:
        cur = stack.pop()
        visited[cur] = 1

        for next in dict[cur]:
            if not visited[next]:
                stack.append(next)


for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, descendent_dict)
    dfs(i, ascendent_dict)
    print(visited.count(0) - 1)
