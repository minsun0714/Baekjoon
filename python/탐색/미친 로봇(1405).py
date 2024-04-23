from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
possibility = list(map(int, s.readline().split()))
n = possibility.pop(0)
possibility = [p / 100 for p in possibility]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def back_tracking(selected, depth, x, y):
    global answer
    if depth == n:
        answer += selected
        return

    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny]:
            continue
        back_tracking(selected * possibility[i], depth + 1, nx, ny)
        visited[nx][ny] = 0


visited = [[0] * (2 * n) for _ in range(2 * n)]
answer = 0

back_tracking(1, 0, n // 2, n // 2)
print(answer)
