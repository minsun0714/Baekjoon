from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(f.readline().strip())
board = [list(map(int, f.readline().strip())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if board[x][y] == 0:
        return False

    board[x][y] = 0
    global house
    house += 1

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return house


count = 0
houses = []
for i in range(n):
    for j in range(n):
        house = 0
        res = dfs(i, j)
        if res:
            houses.append(res)
            count += 1

houses.sort()
print(count)
for house in houses:
    print(house)
