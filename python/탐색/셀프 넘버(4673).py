from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
nums = [1] * 10001


def d(n):
    acc = n
    while n // 10 > 0:
        acc += (n % 10)
        n //= 10
    if n + acc > 10000:
        return
    nums[n + acc] = 0
    d(n + acc)


for i in range(1, 10001):
    if nums[i]:
        d(i)
for i in range(1, 10001):
    if nums[i]:
        print(i)
