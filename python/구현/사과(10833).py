from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, s.readline().split())))
answer = 0
for stu, apple in arr:
    answer += (apple % stu)
print(answer)
