from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

dict = {}
board = [list(map(int, s.readline().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dict[board[i][j]] = (i, j)


def is_bingo():
    count_bingo = 0

    for i in range(5):
        count = 0
        for j in range(5):
            if board[i][j] == 0:
                count += 1
        if count == 5:
            count_bingo += 1

    for j in range(5):
        count = 0
        for i in range(5):
            if board[i][j] == 0:
                count += 1
        if count == 5:
            count_bingo += 1

    count = 0
    for i in range(5):
        if board[i][i] == 0:
            count += 1
        if count == 5:
            count_bingo += 1

    count = 0
    for i in range(5):
        if board[i][4 - i] == 0:
            count += 1
        if count == 5:
            count_bingo += 1

    return count_bingo


for i in range(5):
    nums = list(map(int, s.readline().split()))
    for num in nums:
        x, y = dict[num]
        board[x][y] = 0

        if is_bingo() >= 3:
            print(i * 5 + nums.index(num) + 1)
            exit()
