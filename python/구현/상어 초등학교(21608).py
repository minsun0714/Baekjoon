from sys import stdin as s
import heapq


s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def count_likes(x, y):
    likes = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if board[nx][ny] in friends:
            likes += 1
    return likes


def count_blank_seats(x, y):
    blank = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if board[nx][ny] == 0:
            blank += 1

    return blank


def count_prefered_seat(student):
    seats = []
    heapq.heapify(seats)

    for x in range(n):
        for y in range(n):
            if board[x][y]:
                continue

            likes = count_likes(x, y)
            blank = count_blank_seats(x, y)

            heapq.heappush(seats, [-likes, -blank, x, y])
    [likes, blank, x, y] = heapq.heappop(seats)
    board[x][y] = student


def get_score(x, y, friends):
    score = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if board[nx][ny] in friends:
            score += 1
    score = int(10 ** (score - 1))
    return score


board = [[0] * n for _ in range(n)]
dict = {}
for _ in range(n ** 2):
    arr = list(map(int, s.readline().split()))
    student = arr.pop(0)

    friends = {}
    for friend in arr:
        friends[friend] = True
    dict[student] = friends
    count_prefered_seat(student)

answer = 0
for i in range(n):
    for j in range(n):
        score = get_score(i, j, dict[board[i][j]])
        answer += score
print(answer)
