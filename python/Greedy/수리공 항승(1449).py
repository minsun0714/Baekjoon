from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, l = map(int, s.readline().split())

spots = list(map(int, s.readline().split()))

answer = 0
spots.sort()

while spots:
    start = spots.pop()
    while spots and start - spots[len(spots) - 1] < l:
        spots.pop()
    answer += 1

print(answer)
