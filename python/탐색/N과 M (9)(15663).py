from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))
arr.sort()


def back_tracking(selected, depth):
    if depth == m:
        print(*selected)
        return
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1] and not visited[i - 1]:
            continue
        if not visited[i]:
            visited[i] = 1
            back_tracking(selected + [arr[i]], depth + 1)
            visited[i] = 0


visited = [0] * n
back_tracking([], 0)
