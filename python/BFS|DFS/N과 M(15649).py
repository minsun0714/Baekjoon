from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
visited = [0] * (n + 1)


def dfs(depth, visited, nums=[]):
    # print(depth, visited, nums)
    if depth == m:
        # nums를 문자열로
        print(' '.join(map(str, nums)))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(depth + 1, visited, nums + [i])
        visited[i] = 0


dfs(0, visited)
