from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

nums = []
for i in range(n):
    nums.append(int(s.readline().strip()))

nums.sort()

for i in nums:
    print(i)
