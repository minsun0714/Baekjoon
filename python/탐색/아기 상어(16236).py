from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def bfs(x, y):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    shark_size = 2
    eat_count = 0
    time = 0

    heap_q = [(0, x, y)]
    heapq.heapify(heap_q)

    visited = [[0] * n for _ in range(n)]

    while heap_q:
        depth, x, y = heapq.heappop(heap_q)

        if 0 < board[x][y] < shark_size:
            time = depth
            board[x][y] = 0
            heap_q = [(0, x, y)]
            visited = [[0] * n for _ in range(n)]
            eat_count += 1

        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1

            if board[nx][ny] > shark_size:
                continue

            heapq.heappush(heap_q, (depth + 1, nx, ny))

    print(time)


for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            bfs(i, j)
