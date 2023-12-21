from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())

not_heard = {}
for _ in range(n):
    not_heard[s.readline().strip()] = True

not_heard_not_seen = []
for _ in range(m):
    cur = s.readline().strip()
    if cur in not_heard:
        not_heard_not_seen.append(cur)

not_heard_not_seen.sort()
length = len(not_heard_not_seen)
print(length)
for name in not_heard_not_seen:
    print(name)
