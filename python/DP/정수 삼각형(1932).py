from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

triangle = []

for i in range(n):
    triangle.append(list(map(int, s.readline().strip().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]

        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]

        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i - 1][j])

print(max(triangle[n-1]))
