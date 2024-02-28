from sys import stdin as f
from collections import deque

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분
t = int(f.readline())


def D(n):
    int_num = int(n)
    return str((2 * int_num) % 10000)


def S(n):
    int_num = int(n)
    return str(int_num - 1 if int_num > 0 else 9999)


def L(n):
    str_num = str(n)
    while len(str_num) < 4:
        str_num = '0' + str_num
    first = str_num[0]
    return str_num[1:] + first


def R(n):
    str_num = str(n)
    while len(str_num) < 4:
        str_num = '0' + str_num
    last = str_num[-1]
    return last + str_num[:-1]


def bfs(x):

    q = deque([(x, '')])

    while q:
        (x, funcs) = q.popleft()

        for i in range(4):
            nx = int(func_list[i](x))

            if visited[nx]:
                continue
            visited[nx] = True

            if nx == b:
                return funcs + func_list[i].__name__
            q.append((str(nx), funcs + func_list[i].__name__))


for _ in range(t):
    a, b = map(int, f.readline().split())
    func_list = [D, S, L, R]
    visited = [False] * 10001
    visited[a] = True
    res = bfs(a)
    print(res)
