from sys import stdin as f
from itertools import combinations

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(f.readline().rstrip())
arr = []

for i in range(1, 11):
    comb = list(combinations(range(10), i))
    nums = []
    for j in comb:
        nums.append(sorted(j, reverse=True))
    nums.sort()
    arr.extend(nums)
if n >= len(arr):
    print(-1)
    exit(0)

print(''.join(map(str, arr[n])))
