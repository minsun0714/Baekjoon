from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
m = int(s.readline().strip())
buttons_not_working = list(map(int, s.readline().strip().split()))
# buttons_working = [i for i in range(10) if i not in buttons_not_working]
# answer = 1e9


# def brutal_force(depth, channel):
#     if depth == len(str(n)) or depth == len(str(n)) + 1:
#         global answer
#         answer = min(answer, abs(int(channel) - n))
#         if depth == len(str(n)) + 1:
#             return

#     for i in range(len(buttons_working)):
#         brutal_force(depth + 1, channel + str(buttons_working[i]))

#     return answer


# result = brutal_force(0, "")
# answer = min(result + len(str(n)), abs(n - 100))
# print(answer)
answer = abs(n - 100)


def is_possible(channel):
    for ch in str(channel):
        if int(ch) in buttons_not_working:
            return False
    return True


for i in range(1000001):  # 모든 경우의 수를 확인
    if is_possible(i):
        # 버튼을 누르는 횟수와 +, - 버튼을 누르는 횟수의 합을 계산
        press = len(str(i)) + abs(n - i)
        answer = min(answer, press)

print(answer)
