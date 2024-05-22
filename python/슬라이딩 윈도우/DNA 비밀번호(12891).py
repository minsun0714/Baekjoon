from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분
s, p = map(int, f.readline().split())

dna_string = list(f.readline().strip())
a, c, g, t = map(int, f.readline().split())


dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

l = 0
count = 0
for r in range(s):
    if dna_string[r] in dict:
        dict[dna_string[r]] += 1
    if r >= p - 1:
        if dict['A'] >= a and dict['C'] >= c and dict['G'] >= g and dict['T'] >= t:
            count += 1
        dict[dna_string[l]] -= 1
        l += 1


print(count)
