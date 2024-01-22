from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
cards = list(map(int, s.readline().split()))


m = int(s.readline().strip())
nums = list(map(int, s.readline().split()))

cards.sort()


def binary_search(cards, target, start, end):
    # 왜 start == end일 때도 탐색을 해야하는가?
    # start == end일 때, cards[mid] == target이면 1을 리턴하고
    # cards[mid] != target이면 0을 리턴한다.
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == target:
            return 1
        elif cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for num in nums:
    res = binary_search(cards, num, 0, n - 1)
    print(res, end=' ')
