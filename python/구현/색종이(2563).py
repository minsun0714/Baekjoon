from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

papers = [list(map(int, s.readline().split())) for _ in range(n)]
board = [[0] * 100 for _ in range(100)]


def point_dots(x, y):
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1


for x, y in papers:
    point_dots(x, y)

answer = 0
for row in board:
    answer += row.count(1)

print(answer)
