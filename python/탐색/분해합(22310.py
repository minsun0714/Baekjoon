from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

for i in range(1, n + 1):
    num = i
    acc = i
    while num > 0:
        acc += (num % 10)
        num //= 10

    if acc == n:
        print(i)
        break

    if i == n:
        print(0)
