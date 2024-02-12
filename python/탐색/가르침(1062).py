from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, k = map(int, s.readline().split())
if k < 5:
    print(0)
    exit(0)

ans = 0


def check_if_readable(word, useable):
    mid_word = word[4:-4]

    for a in mid_word:
        if not useable[ord(a) - 97]:
            return False
    return True


def back_tracking(depth, useable, start):
    if depth == k - 5:
        count = 0
        for word in words:
            if check_if_readable(word, useable):
                count += 1
        global ans
        ans = max(ans, count)

        return

    for i in range(start, 26):
        if not useable[i]:
            useable[i] = True
            back_tracking(depth + 1, useable, i + 1)
            useable[i] = False


words = [s.readline().strip() for _ in range(n)]
ans = 0

useable = [False] * 26
common_alps = 'antic'
for c in common_alps:
    useable[ord(c) - 97] = True
back_tracking(0, useable, 0)
print(ans)
