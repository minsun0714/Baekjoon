from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = list(map(int, s.readline().strip().split()))

city = []
for i in range(n):
    city.append(list(map(int, s.readline().strip().split())))

chicken = []

house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

visited = [0] * len(chicken)


def chicken_distance(chicken_candidates):
    total_distance = 0
    for (x, y) in house:
        min_distance = 1e9
        for (i, j) in chicken_candidates:
            distance = abs(i - x) + abs(j - y)
            min_distance = min(min_distance, distance)
        total_distance += min_distance

    return total_distance


result = 1e9


def dfs(depth, start, chicken_candidates):
    if depth == m:
        total_distance = chicken_distance(chicken_candidates)
        global result
        result = min(result, total_distance)

        return

    for i in range(start, len(chicken)):
        if not visited[i]:
            visited[i] = 1
            chicken_candidates.append(chicken[i])
            dfs(depth + 1, i + 1, chicken_candidates)
            chicken_candidates.pop()
            visited[i] = 0

    return result


print(dfs(0, 0, []))
