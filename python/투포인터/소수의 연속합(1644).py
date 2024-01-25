from sys import stdin as s
import math

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
if n == 1:
    print(0)
    exit(0)


def get_prime_numbers(n):  # 에라토스테네스의 체
    prime_numbers = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            prime_numbers[i * j] = False
            j += 1

    return [i for i in range(2, n + 1) if prime_numbers[i]]


def two_pointer():
    prime_numbers = get_prime_numbers(n)

    start, end = 0, 0
    partial_sum = prime_numbers[0]

    ans = 0

    while start <= end:
        if partial_sum < n:
            if prime_numbers[end] < prime_numbers[-1]:
                end += 1
                partial_sum += prime_numbers[end]
            else:
                break

        else:
            if (partial_sum == n):
                ans += 1
            partial_sum -= prime_numbers[start]
            start += 1

    return ans


print(two_pointer())
