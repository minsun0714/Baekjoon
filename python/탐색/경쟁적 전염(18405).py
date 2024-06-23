from sys import stdin as f
from collections import deque
import heapq

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, k = map(int, f.readline().split())
board = [list(map(int, f.readline().split())) for _ in range(n)]
s, x, y = map(int, f.readline().split())


def spread(heap_q):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while heap_q:
        second, virus, i, j = heapq.heappop(heap_q)

        if second == s:
            break

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue

            if board[ni][nj]:
                continue

            board[ni][nj] = virus

            heapq.heappush(heap_q, (second + 1, virus, ni, nj))


heap_q = []
heapq.heapify(heap_q)
for i in range(n):
    for j in range(n):
        if board[i][j]:
            heapq.heappush(heap_q, (0, board[i][j], i, j))
spread(heap_q)
print(board[x - 1][y - 1])
