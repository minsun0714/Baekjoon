from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
g = defaultdict(list)
for i in range(1, n + 1):
    g[int(s.readline())].append(i)

checked = [False] * (n + 1)
result = []


def dfs(node, visited):
    visited.add(node)
    checked[node] = True

    for v in g[node]:
        if not v in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return


for node in range(1, n + 1):
    if not checked[node]:
        dfs(node, set([]))

result.sort()

print(len(result))
for i in result:
    print(i)
