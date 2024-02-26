from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
t = int(s.readline())

for _ in range(t):
    n = int(s.readline())
    note1 = sorted(list(map(int, s.readline().split())))
    m = int(s.readline())
    note2 = list(map(int, s.readline().split()))

    def binary_search(start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if note1[mid] == target:
                print(1)
                return
            elif note1[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        print(0)

    for num in note2:
        binary_search(0, n-1, num)
