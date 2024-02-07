from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, s = map(int, f.readline().split())
nums = list(map(int, f.readline().split()))

ans = 0


def dfs(num, depth, start):
    if sum(num) == s and num:
        global ans
        ans += 1

    if depth == n:
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(num + [nums[i]], depth + 1, i + 1)
            visited[i] = False


visited = [False] * n
dfs([], 0, 0)
print(ans)
