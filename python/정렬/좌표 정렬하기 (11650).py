from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

coordinates = []
for i in range(n):
    coordinates.append(list(map(int, s.readline().strip().split())))

coordinates.sort(key=lambda x: (x[0], x[1]))

for [x, y] in coordinates:
    print(x, y)
