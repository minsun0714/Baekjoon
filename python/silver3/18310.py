from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

houses = list(map(int, s.readline().strip().split()))

houses.sort()

print(houses[(n - 1) // 2])
