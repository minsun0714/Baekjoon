from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())

temperatures = list(map(int, s.readline().split()))
answer = -1e9

window = 0
l = 0
for r in range(n):
    window += temperatures[r]

    if r >= k:
        window -= temperatures[l]
        l += 1
    if r >= k - 1:
        answer = max(answer, window)
print(answer)
