from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
mp, mf, ms, mv = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]
answer = 1e9
ingredients = []


def satisfy_min_ingredients(selected):
    if sum([board[i][0] for i in selected]) >= mp and sum([board[i][1] for i in selected]) >= mf and sum([board[i][2] for i in selected]) >= ms and sum([board[i][3] for i in selected]) >= mv:
        return True
    return False


def back_tracking(selected, depth, x):
    global answer, ingredients
    if satisfy_min_ingredients(selected):
        if sum([board[i][4] for i in selected]) < answer:
            answer = min(answer, sum([board[i][4] for i in selected]))
            ingredients = [i + 1 for i in selected]
    if depth == n:
        return

    for i in range(x, n):
        back_tracking(selected + [i], depth + 1, i + 1)


back_tracking([], 0, 0)

if answer == 1e9:
    print(-1)
else:
    print(answer)
    print(*ingredients)
