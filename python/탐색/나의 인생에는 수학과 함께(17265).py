from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
board = [s.readline().split() for _ in range(n)]

dx, dy = [0, 1], [1, 0]


def calculate(acc, operand, new):
    new = int(new)
    if operand == '+':
        return acc + new
    elif operand == '-':
        return acc - new
    else:
        return acc * new


max_v, min_v = -1e9, 1e9


def dfs(x, y, depth, acc, operand):
    if depth == 2 * n - 2:
        global max_v, min_v
        max_v = max(max_v, acc)
        min_v = min(min_v, acc)
        return
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        new = board[nx][ny]
        new_acc = acc

        if depth % 2:
            new_acc = calculate(acc, operand, new)
        else:
            operand = new

        dfs(nx, ny, depth + 1, new_acc, operand)


dfs(0, 0, 0, int(board[0][0]), '')
print(max_v, min_v)
