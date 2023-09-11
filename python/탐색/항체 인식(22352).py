from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())

before = [list(map(int, s.readline().split())) for _ in range(n)]
after = [list(map(int, s.readline().split())) for _ in range(n)]

x, y = 0, 0
is_different = False
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            x, y = i, j
            is_different = True
            break
    if is_different:
        break
if not is_different:
    print('YES')
    exit(0)

prev_value = before[x][y]
next_value = after[x][y]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if before[x][y] != prev_value:
        return False

    before[x][y] = next_value

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return True


dfs(x, y)

for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            print('NO')
            exit(0)
print('YES')
