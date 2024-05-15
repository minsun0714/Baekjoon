from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
nums = list(map(int, s.readline().split()))
operators = list(map(int, s.readline().split()))


def back_tracking(selected, depth):
    global max_val, min_val
    if depth == n:
        max_val = max(max_val, selected)
        min_val = min(min_val, selected)
        return
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            temp = selected
            if i == 0:
                selected += nums[depth]
            elif i == 1:
                selected -= nums[depth]
            elif i == 2:
                selected *= nums[depth]
            else:
                if nums[depth]:
                    if selected < 0 and nums[depth] > 0:
                        selected = -(-selected // nums[depth])
                    elif selected > 0 and nums[depth] < 0:
                        selected = -(selected // -nums[depth])
                    else:
                        selected //= nums[depth]
                else:
                    continue

            back_tracking(selected, depth + 1)
            selected = temp
            operators[i] += 1


max_val = -1e9
min_val = 1e9
back_tracking(nums[0], 1)
print(max_val)
print(min_val)
