from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분


def bfs(test_case):
    q = deque()
    q.append([home_x, home_y])
    visited = [False] * n

    while q:
        x, y = q.popleft()
        if abs(fest_x - x) + abs(fest_y - y) <= 1000:
            return 'happy'

        for i in range(n):
            if not visited[i]:
                new_x, new_y = test_case[i]
                if abs(new_x - x) + abs(new_y - y) <= 1000:
                    q.append(test_case[i])
                    visited[i] = True
                    # break문을 걸면 안된다.
                    # break

    return 'sad'


t = int(s.readline().strip())
for _ in range(t):
    test_case = []
    n = int(s.readline().strip())
    home_x, home_y = map(int, s.readline().split(' '))
    for _ in range(n):
        test_case.append((list(map(int, s.readline().split(' ')))))
    fest_x, fest_y = map(int, s.readline().split(' '))
    print(bfs(test_case))
