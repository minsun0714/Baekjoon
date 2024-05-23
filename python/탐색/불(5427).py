from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

t = int(s.readline())


def bfs(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    heap_q = arr

    while heap_q:
        depth, is_sanggeun, x, y = heapq.heappop(heap_q)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                if is_sanggeun:
                    print(depth)
                    return True
                else:
                    continue

            if board[nx][ny] == '#':
                continue

            if visited[nx][ny][0] or visited[nx][ny][1]:
                continue

            visited[nx][ny][is_sanggeun] = visited[x][y][is_sanggeun] + 1
            heapq.heappush(heap_q, (depth + 1, is_sanggeun, nx, ny))

    return False


for _ in range(t):
    w, h = map(int, s.readline().split())
    board = [list(map(str, s.readline().strip())) for _ in range(h)]

    arr = []
    heapq.heapify(arr)
    visited = [[[0, 0] for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                visited[i][j][1] = 1
                heapq.heappush(arr, (1, 1, i, j))
            elif board[i][j] == '*':
                visited[i][j][0] = 1
                heapq.heappush(arr, (1, 0, i, j))

    if not bfs(arr):
        print('IMPOSSIBLE')
