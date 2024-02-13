from sys import stdin as s
from collections import defaultdict

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
dict = defaultdict(list)
for _ in range(n):
    cur, left_c, right_c = s.readline().strip().split(' ')
    dict[cur].append(left_c)
    dict[cur].append(right_c)


def pre_order(cur):
    visited[ord(cur) - 65] = True
    global ans
    ans += cur

    for next in dict[cur]:
        if next != '.' and not visited[ord(next) - 65]:
            pre_order(next)


visited = [False] * n
ans = ''
pre_order('A')
print(ans)


def in_order(cur):

    for next in dict[cur]:
        if next != '.' and not visited[ord(next) - 65]:
            in_order(next)
        if not visited[ord(cur) - 65]:
            global ans
            ans += cur
        visited[ord(cur) - 65] = True


visited = [False] * n
ans = ''
in_order('A')
print(ans)


def post_order(cur):
    visited[ord(cur) - 65] = True

    for next in dict[cur]:
        if next != '.' and not visited[ord(next) - 65]:
            post_order(next)

    # 더 이상 방문할 자식 노드가 없을 때 현재 노드를 방문
    global ans
    ans += cur


visited = [False] * n
ans = ''
post_order('A')
print(ans)
