from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, k = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))
nums.sort(reverse=True)
print(sum(nums[:k]) - sum([i for i in range(k)]))
