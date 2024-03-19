from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())

people = list(map(int, s.readline().strip().split()))
arr = [0] * n

for i in range(1, n + 1):
    person = people[i-1]
    for j in range(n):
        if not arr[j] and person == 0:
            arr[j] = i
            break
        if not arr[j]:
            person -= 1

for el in arr:
    print(el, end=" ")
