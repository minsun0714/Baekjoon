from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분


def bfs(building):
    dw = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    q = deque([(sw, sx, sy)])
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    while q:
        w, x, y = q.popleft()
        for i in range(6):
            nw = w + dw[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nw < 0 or nx < 0 or ny < 0 or nw >= l or nx >= r or ny >= c:
                continue
            if building[nw][nx][ny] == '#':
                continue
            if visited[nw][nx][ny]:
                continue

            visited[nw][nx][ny] = visited[w][x][y] + 1
            if visited[ew][ex][ey]:
                x = str(visited[ew][ex][ey])
                print('Escaped in ' + x + ' minute(s).')
                return

            q.append((nw, nx, ny))

    print('Trapped!')


while True:
    l, r, c = map(int, s.readline().split())
    if l == 0:
        break
    building = []
    sw, sx, sy = 0, 0, 0
    ew, ex, ey = 0, 0, 0
    for i in range(l):
        floor = []
        for j in range(r):
            row = list(map(str, s.readline().strip()))
            floor.append(row)
            if 'S' in row:
                sw, sx, sy = i, j, row.index('S')
            if 'E' in row:
                ew, ex, ey = i, j, row.index('E')
        building.append(floor)
        s.readline().strip()

    bfs(building)
