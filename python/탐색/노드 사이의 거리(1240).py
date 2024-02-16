from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
dict = defaultdict(list)

for _ in range(n - 1):
    a, b, d = map(int, s.readline().split())
    dict[a].append((b, d))
    dict[b].append((a, d))


def dfs(start, end):
    stack = [(start, 0)]

    while stack:
        cur_node, cur_d = stack.pop()
        if cur_node == end:
            return

        for next in dict[cur_node]:
            next_node, next_d = next
            if not visited[next_node]:
                visited[next_node] = visited[cur_node] + next_d
                stack.append(next)


for _ in range(m):
    u, v = map(int, s.readline().split())
    visited = [0] * (n + 1)
    dfs(u, v)
    print(visited[v])
