from sys import stdin as f
from collections import defaultdict

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, f.readline().rstrip().split())
dic = defaultdict(list)

for _ in range(m):
    a, b = map(int, f.readline().rstrip().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0] * n


def dfs(depth, node):
    if depth == 5:
        print(1)
        exit(0)

    for next_node in dic[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(depth + 1, next_node)
            visited[next_node] = 0


for i in range(n):
    dfs(0, i)
print(0)
