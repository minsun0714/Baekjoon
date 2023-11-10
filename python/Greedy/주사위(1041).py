from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline())
nums = list(map(int, s.readline().split()))

# 마주보는 면들을 쌍으로 두고, 각 쌍에서 최소값을 list에 저장
# list에 3개의 값이 저장되면, 그 중 최소값은 1면이 보이는 주사위에 보일 값이 된다.
# 2번째로 작은 값을 꺼내면, 최소값인 면과 마주보지 않는 면들 중 가장 작은 값을 고를 수 있다.
# 나머지 3번째 값을 꺼내면, 1번째 또는 2번쨰 값과 마주보지 않는 면들 중 가장 작은 값을 고를 수 있다.
# 이렇게 3개의 값을 꺼낸 후, 각 면들이 필요한 주사위의 개수를 각각 곱한다.

if n == 1:
    nums.sort()
    nums.pop()
    print(sum(nums))
    exit(0)

mins_list = [min(nums[0], nums[5]), min(
    nums[1], nums[4]), min(nums[2], nums[3])]

mins_list.sort()

first_min = mins_list[0]
second_mins = first_min + mins_list[1]
third_mins = second_mins + mins_list[2]

count_one_side = 4 * (n - 2) * (n - 1) + (n - 2) * (n - 2)
count_two_sides = 4 * (n - 1) + 4 * (n - 2)
count_three_sides = 4

result = count_one_side * first_min + count_two_sides * \
    second_mins + count_three_sides * third_mins
print(result)
