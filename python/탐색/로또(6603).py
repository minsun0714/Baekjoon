from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분


def brute_force(depth, start):
    if depth == 6:
        print(*result)
        return
    for i in range(start, n):
        result[depth] = nums[i]
        brute_force(depth + 1, i + 1)


while True:
    nums = list(map(int, s.readline().split()))
    n = nums.pop(0)
    if n == 0:
        break
    result = [0] * 6
    brute_force(0, 0)
    print()
