from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

a, b = map(int, s.readline().split())

count = 1

while b > a:
    if b % 10 == 1:
        b //= 10
    else:
        b /= 2
    count += 1

print(count if a == b else -1)
