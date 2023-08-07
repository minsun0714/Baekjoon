from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
input = list(s.readline().strip())
current_dir = 0
# 남 서 북 동
dir_dic = {'L': -1, 'R': 1, 'F': 0}
go_forward_dic = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}
x, y = (0, 0)


def turn_90_degrees(L_or_R, current_dir):
    current_dir += dir_dic[L_or_R]
    if current_dir == -1:
        current_dir = 3
    elif current_dir == 4:
        current_dir = 0
    return current_dir


walk_record = [(0, 0)]
for i in input:
    current_dir = turn_90_degrees(i, current_dir)

    if i != 'F':
        continue

    x, y = x + go_forward_dic[current_dir][0], y + \
        go_forward_dic[current_dir][1]
    walk_record.append((x, y))

# x좌표에서 가장 작은 값, y좌표에서 가장 작은 값을 구하면 된다.
min_x = min(walk_record, key=lambda x: x[0])[0]
min_y = min(walk_record, key=lambda x: x[1])[1]
max_x = max(walk_record, key=lambda x: x[0])[0]
max_y = max(walk_record, key=lambda x: x[1])[1]

row_length, col_length = max_x - min_x + 1, max_y - min_y + 1
board = [['#' for _ in range(col_length)] for _ in range(row_length)]

for (i, j) in walk_record:
    i += abs(min_x)
    j += abs(min_y)
    board[i][j] = '.'

for row in board:
    print(''.join(row))
