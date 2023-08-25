from sys import stdin as s
from collections import deque

s=open("input.txt","rt") # 주석 처리해야 하는 부분

n, m, k, x = list(map(int, s.readline().split()))

array = []
for i in range(m): # n이 아니라 m으로 범위를 지정할 것
    array.append(list(map(int, s.readline().split())))

graph = [[] for _ in range(n + 1)]
for [A, B] in array:
    graph[A].append(B)

distance = [-1 for _ in range(n + 1)]
distance[x] = 0

def bfs():
    queue = deque([x])

    while queue:
        currNode = queue.popleft()

        for nextNode in graph[currNode]:
            if distance[nextNode] == -1:
                distance[nextNode] = distance[currNode] + 1
                queue.append(nextNode)

    return distance

distance = bfs()

count = 0
for i in range(n + 1):
    if distance[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)