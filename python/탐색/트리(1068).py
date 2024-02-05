from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
nodes = list(map(int, s.readline().split()))
node_to_delete = int(s.readline().strip())
root = nodes.index(-1)
if root == node_to_delete:
    print(0)
    exit(0)

dict = defaultdict(list)
for i in range(n):
    if nodes[i] == -1:
        continue
    dict[nodes[i]].append(i)


def dfs(count_leaf):
    visited = [False] * n
    stack = [root]

    while stack:
        cur = stack.pop()

        if not visited[cur]:
            visited[cur] = True
            if len(dict[cur]) == 0 or dict[cur] == [node_to_delete]:
                count_leaf += 1
            for next in dict[cur]:
                if next == node_to_delete:
                    continue
                stack.append(next)

    return count_leaf


ans = dfs(0)
print(ans)
