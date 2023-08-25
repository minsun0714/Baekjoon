from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())

lectures = []
for _ in range(n):
    lectures.append(list(map(int, s.readline().split())))
# 시작 시간을 기준으로 정렬. 근데 why?
lectures.sort(key=lambda x: x[0])

room_count = 1
end_times = [lectures.pop(0)[1]]
# 각 강의실의 종료 시각들을 관리할 리스트에서 최소힙을 이용하여 가장 빨리 끝나는 시각을 꺼낼 예정
heapq.heapify(end_times)

for lecture in lectures:
    [new_start_time, new_end_time] = lecture

    # 최소 힙을 이용하여 마지막 수업이 가장 빨리 끝나는 강의실의 강의 종료 시각을 min_end_time에 할당
    min_end_time = heapq.heappop(end_times)

    # 새로운 강의 시작 시간이 기존 가장 일찍 끝나는 시각보다 이르면 강의실 개수를 늘리고 end_times 배열에서 종료 시각을 하나 더 관리해야 함.
    if min_end_time > new_start_time:
        room_count += 1
        heapq.heappush(end_times, min_end_time)

    # 대소비교 결과와 무관히 원본 heapq에서 꺼냈던 가장 이른 종료 시각을 heapq에 다시 heappush한다.
    heapq.heappush(end_times, new_end_time)

print(room_count)
