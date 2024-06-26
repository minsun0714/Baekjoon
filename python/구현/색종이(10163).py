from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
board = [[0] * 1001 for _ in range(1001)]

for p in range(1, n + 1):
    x, y, w, h = map(int, s.readline().split())

    for i in range(x, x + w):
        for j in range(y, y + h):
            board[i][j] = p
answer = [0] * (n + 1)

for p in range(1, n + 1):
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == p:
                answer[p] += 1
for a in answer[1:]:
    print(a)
