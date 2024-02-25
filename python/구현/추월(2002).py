from sys import stdin as s
from collections import deque
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
order = deque([])
tunnel = deque([])
for i in range(2 * n):
    if i < n:
        order.append(s.readline().strip())
    else:
        tunnel.append(s.readline().strip())

count = 0
checked = defaultdict(bool)

while tunnel:
    cur = tunnel.popleft()
    checked[cur] = True

    if cur == order[0]:
        order.popleft()

    else:
        if checked[order[0]]:
            order.popleft()
            tunnel.appendleft(cur)
        else:
            count += 1

print(count)
