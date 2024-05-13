from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
n = int(s.readline())
scores = list(map(int, s.readline().split()))
scores.sort()
answer = 0
for i in range(n):
    s, e = i + 1, n - 1

    while s < e:
        if scores[i] + scores[s] + scores[e] == 0:
            if scores[s] == scores[e]:
                answer += (e - s + 1) * (e - s) // 2
                break
            else:
                count_s, count_e = 1, 1
                while s + 1 < e and scores[s] == scores[s + 1]:
                    s += 1
                    count_s += 1
                while s < e - 1 and scores[e] == scores[e - 1]:
                    e -= 1
                    count_e += 1
                answer += count_s * count_e
                s += 1
                e -= 1

        elif scores[i] + scores[s] + scores[e] > 0:
            e -= 1
        else:
            s += 1
print(answer)
