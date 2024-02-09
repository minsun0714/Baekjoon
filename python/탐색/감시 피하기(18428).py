from sys import stdin as s
import copy

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
board = [list(map(str, s.readline().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
teachers = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))


def can_watch_student(teacher, copied_board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        tx, ty = teacher
        while tx >= 0 and ty >= 0 and tx < n and ty < n:
            if copied_board[tx][ty] == 'O':
                break
            if copied_board[tx][ty] == 'S':
                return False
            tx, ty = tx + dx[i], ty + dy[i]
    return True


def dfs(o_list, depth, start_x, start_y):
    if depth == 3:
        copied_board = copy.deepcopy(board)
        for ox, oy in o_list:
            copied_board[ox][oy] = 'O'

        nobody_watched = False
        for teacher in teachers:
            if not can_watch_student(teacher, copied_board):
                nobody_watched = True
                break
        if not nobody_watched:
            print("YES")
            exit(0)
        return

    # 재귀 호출 시 j + 1을 start_y로 넘겨주는 이유는 같은 행에서는 다음 열부터 탐색해야 하기 때문이다.
    # 새 행으로 넘어갈 때는 start_y를 0으로 초기화해야 한다.

    # 애초에 board에 'O'를 찍고 재귀 호출 아래에서 다시 'X'로 바꿔주는 방식으로 구현하면 board를 복사할 필요가 없고 더 간단해진다.
    for i in range(start_x, n):
        for j in range(start_y, n):
            if board[i][j] == 'X':
                dfs(o_list + [(i, j)], depth + 1, i, j + 1)
        start_y = 0


dfs([], 0, 0, 0)
print("NO")
