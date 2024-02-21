from sys import stdin as s
import sys
sys.setrecursionlimit(10*9)

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())


nums = [i for i in range(10)]


def back_tracking(depth, selected, digit):
    global count
    if depth == digit:
        count += 1
        if count == n:
            answer = ''
            for i in selected:
                answer += str(i)
            print(int(answer))
            exit(0)
        return

    for i in range(10):
        if selected:
            last = selected[-1]
            if i >= last:
                continue
        back_tracking(depth + 1, selected + [i], digit)


count = 0
for k in range(1, 11):
    back_tracking(0, [], k)
print(-1)
