from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
A = list(map(int, s.readline().strip()))
B = list(map(int, s.readline().strip()))


def turn_switch(arr, index):
    arr[index] = 1 if arr[index] == 0 else 0
    return arr


A_copied_first_left = A.copy()

A_copied_first_switched = A.copy()
A_copied_first_switched = turn_switch(A_copied_first_switched, 0)
A_copied_first_switched = turn_switch(A_copied_first_switched, 1)


def iterateArray(A_copied, B, turn_times=0):
    for i in range(1, n):
        if A_copied[i - 1] != B[i - 1]:
            turn_times += 1
            turn_switch(A_copied, i - 1)
            turn_switch(A_copied, i)
            if i < n - 1:
                turn_switch(A_copied, i + 1)

    if "".join(map(str, A_copied)) == "".join(map(str, B)):
        return [A_copied, turn_times]

    return [A_copied, 1e9]


[A_copied_first_switched, turn_times_when_first_switched] = iterateArray(
    A_copied_first_switched, B, 1)
[A_copied_first_left, turn_times_when_first_left] = iterateArray(
    A_copied_first_left, B)
if A_copied_first_switched != B and A_copied_first_left != B:
    print(-1)
    exit(0)

print(min(turn_times_when_first_switched, turn_times_when_first_left))
