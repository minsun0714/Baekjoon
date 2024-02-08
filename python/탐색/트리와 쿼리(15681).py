from sys import stdin as s
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, r, q = map(int, s.readline().split())

dict = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, s.readline().split())
    dict[u].append(v)
    dict[v].append(u)


visited = [0] * (n + 1)


def dfs(node):
    visited[node] = 1

    for next in dict[node]:
        if not visited[next]:
            dfs(next)
            visited[node] += visited[next]

    return visited


dfs(r)

for _ in range(q):
    sub_root = int(s.readline())
    print(visited[sub_root])
