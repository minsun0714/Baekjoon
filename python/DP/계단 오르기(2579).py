from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

stairs = [0] * 302

for i in range(1, n + 1):
    stairs[i] = int(s.readline())

# if (n < 3):
#     print(sum(stairs))
#     exit(0)

dp = [0] * 302
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, n + 1):
    # 2가지 option이 있다.
    # # 이전 계단을 밟고 이번 계단을 밟는 것.
    # option1 = dp[i-3] + max(stairs[i-2], stairs[i-1]) + stairs[i]
    # # 이전 계단을 포기하고 이번 계단을 밟는 것.
    # option2 = dp[i-3] + stairs[i-2] + stairs[i - 1] + stairs[i + 1]
    # # 이전 계단을 포기하고 이번 계단을 밟는 것.
    # if (option1 > option2):
    #     # 이번 계단을 밟는다. (직전 2개 중 하나를 버린다.)
    #     dp[i] = option1
    # else:
    #     # 이번 계단을 밟지 않는다.
    #     dp[i] = dp[i-1]

    # 2가지 option이 있다.
    # 전제: i번째 계단을 밟는다.
    # i-1 번째 계단 포기
    option1 = dp[i-2]
    # i-2 번째 계단 포기
    option2 = dp[i-3] + stairs[i-1]
    dp[i] = max(option1, option2) + stairs[i]

print(dp[n])
