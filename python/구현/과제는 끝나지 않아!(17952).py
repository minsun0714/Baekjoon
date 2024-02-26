from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
assignments = [list(map(int, s.readline().strip().split())) for _ in range(n)]

answer = 0
stack = []

for assignment in assignments:
    if assignment[0] == 1:
        is_taken, a, t = assignment
    else:
        if not stack:
            continue
        a, t = stack.pop()
    t -= 1
    if t == 0:
        answer += a
        continue
    stack.append((a, t))
print(answer)
