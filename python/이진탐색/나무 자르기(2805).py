from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, m = map(int, s.readline().split())
trees = list(map(int, s.readline().split()))
trees.sort()

sum_arr = [0] * n
sum_arr[n - 1] = trees[n - 1]
for i in range(n - 2, -1, -1):
    sum_arr[i] = sum_arr[i + 1] + trees[i]

s, e = 0, n - 1
while s <= e:
    mid = (s + e) // 2
    pieces = sum_arr[mid] - trees[mid] * (n - mid)

    if pieces == m:
        print(trees[mid])
        exit()
    elif pieces > m:
        s = mid + 1
    else:
        e = mid - 1

print((sum_arr[s] - m) // (n - s))
