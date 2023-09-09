from sys import stdin as s
import heapq

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
lectures = [list(map(int, s.readline().split()))[1:] for _ in range(n)]
lectures.sort(key=lambda x: x[0])

end_times = []
heapq.heapify(end_times)
count = 1

for lecture in lectures:
    start_time, end_time = lecture
    if end_times:
        earliest_end_time = heapq.heappop(end_times)
        if start_time < earliest_end_time:
            heapq.heappush(end_times, earliest_end_time)
            count += 1
    heapq.heappush(end_times, end_time)

print(count)
