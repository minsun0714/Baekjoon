from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
t = int(s.readline())


def dfs(i):
    stack = [i]

    while stack:
        cur = stack.pop()

        for next in dict[cur]:
            if visited[next]:
                if visited[next] == visited[cur]:
                    return 'impossible'
                else:
                    continue
            visited[next] = 2 if visited[cur] == 1 else 1
            stack.append(next)

    return "possible"


for _ in range(t):
    n, m = map(int, s.readline().split())
    dict = defaultdict(list)

    for _ in range(m):
        a, b = map(int, s.readline().split())
        dict[a].append(b)
        dict[b].append(a)

    visited = [0] * (n + 1)

    ans = 'possible'

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            if dfs(i) == 'impossible':
                ans = 'impossible'

    print(ans)
