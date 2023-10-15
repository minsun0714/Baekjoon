from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

m, n = map(int, s.readline().split())

board = [list(map(int, s.readline().split())) for _ in range(m)]

stack = []


def dfs(x, y):
    if board[x][y] == 0:
        return False

    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        if x < 0 or x >= m or y < 0 or y >= n:
            continue
        if board[x][y] == 0:
            continue

        board[x][y] = 0

        stack.append((x - 1, y - 1))
        stack.append((x - 1, y))
        stack.append((x - 1, y + 1))
        stack.append((x, y - 1))
        stack.append((x, y + 1))
        stack.append((x + 1, y - 1))
        stack.append((x + 1, y))
        stack.append((x + 1, y + 1))

    return True


answer = 0

for i in range(m):
    for j in range(n):
        if dfs(i, j):
            answer += 1

print(answer)
