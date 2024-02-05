from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline().strip())
nums = list(map(int, s.readline().split()))
temp_operators = list(map(int, s.readline().split()))
operators = []
for i in range(4):
    while temp_operators[i]:
        operators.append(i)
        temp_operators[i] -= 1
visited = [False] * (n - 1)


def get_operated(nums, operator_order):
    acc = nums[0]
    for i in range(len(operator_order)):
        num = nums[i + 1]
        if operator_order[i] == 0:
            acc += num
        elif operator_order[i] == 1:
            acc -= num
        elif operator_order[i] == 2:
            acc *= num
        else:
            if acc < 0 and num > 0:
                acc = abs(acc)
                acc = -1 * (acc // num)
            else:
                acc //= num
    return acc


# 실제 max_res, min_res를 구했을 때 값이 -1e9, 1e9로 나올 경우, 소숫점 이하의 값이 나올 수 있으므로 int형으로 변환해주어야 한다.
max_res = int(-1e9)
min_res = int(1e9)


def dfs(operator_order, depth):
    if depth == n - 1:
        res = get_operated(nums, operator_order)
        global max_res, min_res
        max_res, min_res = max(max_res, res), min(min_res, res)
        return

    for i in range(n - 1):
        if not visited[i]:
            visited[i] = True
            dfs(operator_order + [operators[i]], depth + 1)
            visited[i] = False


dfs([], 0)
print(max_res)
print(min_res)
