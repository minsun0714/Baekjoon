import copy
from sys import stdin as s
import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline().strip())
board = [list(map(int, s.readline().split())) for _ in range(n)]


def dfs(x, y, h):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if copied_board[x][y] < h:
        return False

    copied_board[x][y] = 0

    dfs(x - 1, y, h)
    dfs(x + 1, y, h)
    dfs(x, y - 1, h)
    dfs(x, y + 1, h)

    return True


ans = 0
for i in range(1, 101):
    copied_board = copy.deepcopy(board)
    safe_area = 0
    for j in range(n):
        for k in range(n):
            if dfs(j, k, i):
                safe_area += 1
    ans = max(ans, safe_area)
print(ans)
