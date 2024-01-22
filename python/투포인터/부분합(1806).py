from sys import stdin as f
import sys

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, s = map(int, f.readline().split())
nums = list(map(int, f.readline().split()))

start = 0
end = 0
ans = sys.maxsize
partial_sum = nums[0]

while start <= end and end < n:
    if partial_sum < s:
        if end < n - 1:
            end += 1
            partial_sum += nums[end]
        else:
            break

    else:
        ans = min(ans, end - start + 1)
        partial_sum -= nums[start]
        if start < end:
            start += 1

# 어떤 부분합도 s보다 작은 경우 예외처리 필요
if ans == sys.maxsize:
    print(0)
else:
    print(ans)
