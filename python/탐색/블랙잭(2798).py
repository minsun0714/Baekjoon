from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))


def brute_force(selected, depth, start):
    global answer
    if selected > m:
        return
    if depth == 3:
        answer = max(answer, selected)
        return

    for i in range(start, n):
        brute_force(selected + nums[i], depth + 1, i + 1)


answer = 0
brute_force(0, 0, 0)
print(answer)
