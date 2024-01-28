from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())


def bfs():
    q = deque([n])
    visited = [0] * 100001
    visited[n] = 1

    while q:
        cur = q.popleft()

        if cur == k:
            print(visited[cur] - 1)
            return

        next_nodes = [
            (cur * 2, 0),
            (cur - 1, 1),
            (cur + 1, 1),
        ]

        for next in next_nodes:
            next_loc, next_move = next
            if next_loc < 0 or next_loc > 100000:
                continue
            if not visited[next_loc]:
                visited[next_loc] = visited[cur] + next_move
                q.append(next_loc)


if k <= n:
    print(n - k)
else:
    bfs()
