from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, s.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()


def bfs(start_node=5):
    visited = [-1] * (n + 1)
    visited[0], visited[start_node] = 0, 0
    q = deque([start_node])

    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node] == - 1:
                visited[next_node] = visited[cur_node] + 1
                q.append(next_node)

    return sum(visited)


min_value = 1e9
answer = 0
for start_node in range(1, n + 1):
    result = bfs(start_node)
    if min_value > result:
        answer = start_node
        min_value = result

print(answer)
# 노드 간 최단 거리 구하기
# https://shnoh.tistory.com/15
# https://wikidocs.net/206356
