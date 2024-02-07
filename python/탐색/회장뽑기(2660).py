from sys import stdin as s
from collections import defaultdict
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
dict = defaultdict(list)
while True:
    x, y = map(int, s.readline().split())
    if x == -1:
        break
    dict[x].append(y)
    dict[y].append(x)


def bfs(root):
    q = deque([root])
    visited = [0] * (n + 1)
    visited[root] = 1

    while q:
        cur = q.popleft()

        for next in dict[cur]:
            if not visited[next]:
                visited[next] = visited[cur] + 1
                q.append(next)

    return max([i - 1 for i in visited])


score = 1e9
count = 0
candidates = []
for i in range(1, n + 1):
    score_i = bfs(i)
    if score_i < score:
        score = score_i
        count = 1
        candidates = [i]
    elif score_i == score:
        count += 1
        candidates.append(i)

print(score, count)
print(*candidates)
