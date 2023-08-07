from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

cards = [int(i) for i in s.readline().strip().split()]

cards.sort(reverse=True)
q = deque(cards)

max_value = q.popleft()

# 나머지 원소들의 합산 값
sum_of_rest_values = sum(q)

# 나머지 원소들의 개수
count_rest_values = len(q)

answer = sum_of_rest_values + max_value * count_rest_values
print(answer)
