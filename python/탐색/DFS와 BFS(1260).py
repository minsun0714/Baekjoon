from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m, v = map(int, s.readline().split())

graph = [[] for _ in range(n + 1)]
edges = [list(map(int, s.readline().split())) for _ in range(m)]

for _ in range(m):
    [a, b] = edges.pop(0)
    graph[a].append(b)
    graph[b].append(a)

for el in graph:
    el.sort()


def dfs():
    stack = [v]
    visited = [0] * (n + 1)
    dfs_answer = ""

    while stack:
        current_node = stack.pop()
        if (visited[current_node]):
            continue
        dfs_answer += str(current_node) + " "
        visited[current_node] = 1
        for i in graph[current_node][::-1]:
            if visited[i] == 0:
                stack.append(i)

    print(dfs_answer)


dfs()


def bfs():
    q = deque([v])
    visited = [0] * (n + 1)
    bfs_answer = ""

    while q:
        current_node = q.popleft()
        if (visited[current_node]):
            continue
        bfs_answer += str(current_node) + " "
        visited[current_node] = 1
        for i in graph[current_node]:
            if visited[i] == 0:
                q.append(i)

    print(bfs_answer)


bfs()
