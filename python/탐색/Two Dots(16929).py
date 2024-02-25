from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
board = [list(map(str, s.readline().strip())) for _ in range(n)]


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack = [(x, y, x, y)]

    while stack:
        x, y, prev_x, prev_y = stack.pop()
        cur = board[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            next = board[nx][ny]

            if cur != next:
                continue

            if nx == prev_x and ny == prev_y:
                continue

            if visited[nx][ny]:
                global ans
                ans = 'Yes'
                return

            visited[nx][ny] = True

            stack.append((nx, ny, x, y))

    return


visited = [[False] * m for _ in range(n)]
ans = 'No'
for i in range(n):
    if ans == 'Yes':
        break
    for j in range(m):
        if visited[i][j]:
            continue
        visited[i][j] = True
        dfs(i, j)
print(ans)
