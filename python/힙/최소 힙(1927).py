from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
nums = []
heapq.heapify(nums)

for i in range(n):
    num = int(s.readline().strip())

    if num:
        heapq.heappush(nums, num)
    else:
        if not nums:
            print(0)
            continue
        print(heapq.heappop(nums))
