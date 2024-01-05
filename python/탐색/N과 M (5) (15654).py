from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
arr = map(int, s.readline().split())
arr = sorted(arr)

visited = [False] * (n + 1)


def dfs(visited, nums, depth):
    if depth == m:
        ans = []
        for i in nums:
            ans.append(arr[i - 1])
        print(*ans)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(visited, nums + [i], depth + 1)
            visited[i] = False


dfs(visited, [], 0)
