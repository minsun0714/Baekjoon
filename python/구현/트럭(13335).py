from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n, w, l = map(int, s.readline().split())
trucks = deque(list(map(int, s.readline().split())))
first_truck = {'weight': trucks.popleft(), 'time_left': w}
bridge = deque([first_truck])
time_count = 1
cur_total_weight = first_truck['weight']

while bridge:
    time_count += 1

    for truck in bridge:
        truck['time_left'] -= 1

    if bridge[0]['time_left'] == 0:
        cur_total_weight -= bridge[0]['weight']
        bridge.popleft()

    if trucks:
        next_truck_weight = trucks[0]
        if cur_total_weight + next_truck_weight <= l:
            bridge.append({'weight': trucks.popleft(), 'time_left': w})
            cur_total_weight += next_truck_weight

print(time_count)
