from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

array = []
for i in range(n):
    array.append(s.readline().strip().split())

array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in array:
    print(i[0])
