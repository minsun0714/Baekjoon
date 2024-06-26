from sys import stdin as f
import math

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, k = map(int, f.readline().split())
dict = {}
for i in range(1, 7):
    dict[i] = [0, 0]
for _ in range(n):
    s, y = map(int, f.readline().split())
    dict[y][s] += 1

answer = 0
for i in range(1, 7):
    for j in range(2):
        answer += math.ceil(dict[i][j] / k)
print(answer)
