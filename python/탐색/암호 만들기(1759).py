from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

l, c = map(int, s.readline().split())
alphabet = list(map(str, s.readline().split()))

alphabet.sort()
visited = [False] * c
vowel = {"a", "e", "i", "o", "u"}


def brutal_force(depth, visited, password, start):
    if (depth == l):
        # password에서 모음의 개수 세기
        count_vowel = 0
        for letter in password:
            if letter in vowel:
                count_vowel += 1

        count_consonant = l - count_vowel
        if count_vowel >= 1 and count_consonant >= 2:
            print(password)

        return

    for i in range(start, c):
        if not visited[i]:
            visited[i] = True
            brutal_force(depth + 1, visited, password + alphabet[i], i + 1)
            visited[i] = False


brutal_force(0, visited, "", 0)
