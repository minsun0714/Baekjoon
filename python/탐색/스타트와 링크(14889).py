from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline().strip())
table = [list(map(int, s.readline().split())) for _ in range(n)]


def get_score(team):
    score = 0
    for i in range(n):
        for j in range(n):
            if i in team and j in team:
                score += table[i][j]

    return score


ans = 1e9


def dfs(start_team, depth, start):
    if depth == n / 2:
        link_team = [i for i in range(n) if i not in start_team]
        start_team_score = get_score(start_team)
        link_team_score = get_score(link_team)
        global ans
        ans = min(ans, abs(start_team_score - link_team_score))
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(start_team + [i], depth + 1, i + 1)
            visited[i] = False


visited = [False] * n
dfs([], 0, 0)
print(ans)
