from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, r, c = map(int, s.readline().split())
ans = 0

while n:
    n -= 1

    if r < 2 ** n and c < 2 ** n:
        ans += 2 ** n * 2 ** n * 0

    elif r < 2 ** n and c >= 2 ** n:
        c -= 2 ** n
        ans += 2 ** n * 2 ** n * 1

    elif r >= 2 ** n and c < 2 ** n:
        r -= 2 ** n
        ans += 2 ** n * 2 ** n * 2

    else:
        r -= 2 ** n
        c -= 2 ** n
        ans += 2 ** n * 2 ** n * 3

print(ans)
