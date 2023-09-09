from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

s = f.readline().strip()
t = f.readline().strip()


def dfs(word, depth):
    if depth == len(t) - len(s):
        if word == s:
            print(1)
            exit(0)
        return

    if word[-1] == 'A':
        dfs(word[0:-1], depth + 1)
    if word[0] == 'B':
        dfs(word[::-1][0:-1], depth + 1)


dfs(t, 0)
print(0)
