from sys import stdin as f
from collections import deque

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = list(map(int, f.readline().split()))

examiner = []
for i in range(n):
    examiner.append(list(map(int, f.readline().split())))

target_s, target_x, target_y = list(map(int, f.readline().split()))

q = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    for j in range(n):
        if examiner[i][j]:
            q.append((examiner[i][j], 0, i, j))

q.sort()
q = deque(q)

while q:
    virus, second, x, y = q.popleft()
    if second == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if examiner[nx][ny]:
            continue

        examiner[nx][ny] = virus
        q.append((virus, second + 1, nx, ny))

print(examiner[target_x - 1][target_y - 1])
