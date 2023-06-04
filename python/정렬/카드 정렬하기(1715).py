from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

cards = []
for i in range(n):
    heapq.heappush(cards, int(s.readline()))

result = 0

for i in range(n - 1):
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    sum_val = first_card + second_card
    result += sum_val
    heapq.heappush(cards, sum_val)

print(result)
