from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = list(map(int, s.readline().split()))


def dfs(depth, nums, start):
    if depth == m:
        print(*nums)
        return

    for i in range(start, n + 1):
        dfs(depth + 1, nums + [i], i)


dfs(0, [], 1)
