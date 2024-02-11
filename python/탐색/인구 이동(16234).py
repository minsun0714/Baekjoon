from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, l, r = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def dfs(x, y, union):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            is_union_member = (l <= abs(board[nx][ny] - board[x][y]) <= r)
            if not is_union_member:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            stack.append((nx, ny))
            union.append((nx, ny))

    return union


ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    count_unions = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = dfs(i, j, [])
                sum_u, count_u = 0, 0
                if len(union):
                    count_unions += 1
                    for k, m in union:
                        sum_u += board[k][m]
                        count_u += 1
                    for k, m in union:
                        visited[k][m] = sum_u // count_u

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                board[i][j] = visited[i][j]
    if count_unions:
        ans += 1
    else:
        print(ans)
        exit(0)
