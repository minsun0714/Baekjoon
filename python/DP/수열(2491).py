from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
nums = list(map(int, s.readline().split()))

a, b, c = 0, 0, 0
max_len = 0
for i in range(1, n):
    if nums[i] == nums[i - 1]:
        a = i
        max_len = max(max_len, i - min(a, b, c))
    elif nums[i] > nums[i - 1]:
        c = i
        max_len = max(max_len, i - b)
    elif nums[i] < nums[i - 1]:
        b = i
        max_len = max(max_len, i - c)
print(max_len + 1)
