from sys import stdin as s
import math

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())


def is_prime(num):
    num = int(num)
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def brutal_force(depth, num):
    if depth > 0 and not is_prime(num):
        return
    if depth == n:
        print(num)
        return

    for i in range(1, 10):
        brutal_force(depth + 1, num + str(i))


brutal_force(0, "")
