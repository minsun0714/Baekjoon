from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m, v = map(int, s.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    [node_1, node_2] = list(map(int, s.readline().split()))
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

for node in graph:
    node.sort()


def dfs():
    stack = [v]
    visited = [False] * (n + 1)
    answer = []

    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            visited[cur_node] = True
            answer.append(cur_node)
            for i in graph[cur_node][::-1]:
                stack.append(i)

    print(*answer)


dfs()


def bfs():
    q = deque([v])
    visited = [False] * (n + 1)
    answer = []

    while q:
        cur_node = q.popleft()
        if not visited[cur_node]:
            visited[cur_node] = True
            answer.append(cur_node)
            for i in graph[cur_node]:
                q.append(i)

    print(*answer)


bfs()
