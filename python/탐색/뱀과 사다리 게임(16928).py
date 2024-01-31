from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())

# 뱀 정보는 왜 저장할까?
# 더 낮은 숫자로 이동하면 불리한 거 아니야?
# 이해하기 좋은 케이스: 45 -> 47, 48 -> 24, 25 -> 99
ladders_and_snakes = {}
for _ in range(n + m):
    x, y = map(int, s.readline().split())
    ladders_and_snakes[x] = y


def bfs():
    q = deque([1])
    visited = [0] * 101
    visited[1] = 1

    while q:
        x = q.popleft()

        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            # 처음에 했던 실수: 뱀과 사다리가 있는 노드도 q에 넣었다.
            # 뱀과 사다리가 있는 노드가 x가 되어버리면 x + 1, x + 2, ... x + 6도 q에 들어가게 된다.
            # 따라서 뱀과 사다리가 있는 노드일 경우 곧바로 nx를 갱신해줘야 한다.
            if ladders_and_snakes.get(nx):
                nx = ladders_and_snakes[nx]
            if visited[nx]:
                continue

            visited[nx] = visited[x] + 1
            if nx == 100:
                print(visited[nx] - 1)
                return
            q.append(nx)


bfs()
