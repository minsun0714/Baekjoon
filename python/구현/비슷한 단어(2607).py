from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

cur = list(map(str, s.readline().strip()))
answer = 0

for _ in range(n - 1):
    dict = {}
    for l in cur:
        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1
    next = list(map(str, s.readline().strip()))

    diff_count = 0
    for l in next:
        if l in dict and dict[l]:
            dict[l] -= 1
        else:
            diff_count += 1

    if len(next) < len(cur):
        for key in dict:
            diff_count += dict[key]

    if diff_count <= 1:
        answer += 1
print(answer)
