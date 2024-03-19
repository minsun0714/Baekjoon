from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
t = int(s.readline())

for _ in range(t):
    p = list(s.readline().strip())
    n = int(s.readline())
    arr = s.readline().strip()[1:-1].split(',')
    if n == 0:
        arr = []
    q = deque(arr)

    r_count, d_count = p.count('R'), p.count('D')
    if d_count > n:
        print('error')
        continue

    reverse_flag = 0
    for i in range(len(p)):
        if p[i] == 'D':
            if reverse_flag == 0:
                q.popleft()
            else:
                q.pop()
        else:
            reverse_flag = 1 - reverse_flag
    if r_count % 2 == 1:
        q.reverse()

    answer = '['
    for i in range(len(q)):
        answer += q[i]
        if i == len(q) - 1:
            break
        answer += ','
    answer += ']'

    print(answer)
