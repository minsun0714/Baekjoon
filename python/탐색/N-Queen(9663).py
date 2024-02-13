from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

count = 0
row = [0] * n


def can_be_attacked(i, j):
    for r in range(i):
        if row[r] == j or i - r == abs(j - row[r]):
            return True


def back_tracking(depth):
    if depth == n:
        global count
        count += 1
        return

    for j in range(n):
        if can_be_attacked(depth, j):
            continue
        row[depth] = j
        back_tracking(depth + 1)


back_tracking(0)
print(count)
