from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

r, c = map(int, s.readline().split())
if r == c == 1:
    print(1)
    exit(0)
board = [list(s.readline().strip()) for _ in range(r)]
ans = 0


def dfs(x, y, alphabet_visited, depth):
    cur_alphabet_idx = ord(board[x][y]) - 65
    if alphabet_visited[cur_alphabet_idx]:
        global ans
        ans = max(ans, depth)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        alphabet_visited[cur_alphabet_idx] = True
        dfs(nx, ny, alphabet_visited, depth + 1)
        alphabet_visited[cur_alphabet_idx] = False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
alphabet_visited = [False] * 26

dfs(0, 0, alphabet_visited, 0)
print(ans)
