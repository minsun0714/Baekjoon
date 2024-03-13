from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

dict = defaultdict(list)
leaf_nodes = [1] * (n + 1)

for _ in range(n - 1):
    u, v, w = map(int, s.readline().split())
    dict[u].append((v, w))
    dict[v].append((u, w))
    leaf_nodes[u] = 0


def dfs(root):
    stack = [root]

    while stack:
        cur = stack.pop()

        for next in dict[cur]:
            next_node, d = next
            if not visited[next_node]:
                visited[next_node] = d + visited[cur]
                stack.append(next_node)


answer = 0
for start in range(1, n + 1):
    if not leaf_nodes[start]:
        continue
    visited = [0] * (n + 1)
    visited[start] = 1
    dfs(start)
    answer = max(answer, max(visited))
print(answer - 1)
