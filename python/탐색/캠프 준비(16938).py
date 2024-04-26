from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, l, r, x = map(int, s.readline().split())
a = list(map(int, s.readline().split()))


def back_tracking(selected, depth, start):
    global answer
    if 1 < depth <= n and l <= sum(selected) <= r and max(selected) - min(selected) >= x:
        answer += 1

    for i in range(start, n):
        back_tracking(selected + [a[i]], depth + 1, i + 1)


answer = 0
back_tracking([], 0, 0)
print(answer)
