from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))
arr.sort()


def dfs(depth, start):
    if depth == m:
        print(*box)
        return

    for i in range(start, n):
        box.append(arr[i])
        dfs(depth + 1, i)
        box.pop()


box = []
dfs(0, 0)
