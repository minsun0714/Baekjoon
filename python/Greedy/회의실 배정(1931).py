from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())
confs = [list(map(int, s.readline().split())) for _ in range(n)]

# x[0] 기준의 정렬도 필요한 이유
# 예시
# [11, 11], [10, 11] 순으로 정렬되어 있을 경우
# 회의 둘 다 개최 가능하므로 모두 count되어야 하지만,
# start_time == 10 < previous_end_time == 11이므로 [10, 11]이 count되지 않음
confs.sort(key=lambda x: (x[1], x[0]))

answer = 0
previous_end_time = 0

for conf in confs:
    [start_time, end_time] = conf
    if start_time >= previous_end_time:
        answer += 1
        previous_end_time = end_time

print(answer)
