from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
k = int(s.readline().strip())

apples = []
for i in range(k):
    apples.append(list(map(int, s.readline().split())))

board = [[0] * (n + 1) for _ in range(n + 1)]
for apple in apples:
    board[apple[0]][apple[1]] = 1

l = int(s.readline().strip())
snake_moves = deque()
for i in range(l):
    snake_moves.append(list(s.readline().split()))
for snake_move in snake_moves:
    snake_move[0] = int(snake_move[0])


def turn_dirs(current_dir, left_or_right):
    if left_or_right == "L":
        current_dir = 3 if current_dir == 0 else current_dir - 1
    else:
        current_dir = 0 if current_dir == 3 else current_dir + 1
    return current_dir


def is_apple(board, x, y):
    if board[x][y] == 1:
        return True
    else:
        return False


def is_snake_body(snake, x, y):
    for (snake_x, snake_y) in snake:
        if snake_x == x and snake_y == y:
            return True


def snake_every_second(snake_moves):
    dirs = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    x, y = 1, 1
    current_dir = 0
    snake = deque([(x, y)])
    second = 0

    while True:
        second += 1
        x, y = x + dirs[current_dir][0], y + dirs[current_dir][1]

        if x < 1 or x > n or y < 1 or y > n:
            return second
        if is_snake_body(snake, x, y):
            return second

        snake.append((x, y))

        if is_apple(board, x, y):
            board[x][y] = 0
        else:
            snake.popleft()

        if len(snake_moves) > 0 and snake_moves[0][0] == second:
            current_dir = turn_dirs(current_dir, snake_moves[0][1])
            snake_moves.popleft()


print(snake_every_second(snake_moves))
