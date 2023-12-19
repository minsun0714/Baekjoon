from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n, m = map(int, s.readline().split())
dic_number_key = {}
dic_string_key = {}
for i in range(1, n+1):
    pocketmon = s.readline().strip()
    dic_number_key[i] = pocketmon
    dic_string_key[pocketmon] = i


for q in range(m):
    key = s.readline().strip()
    if key.isdigit():
        print(dic_number_key[int(key)])
        continue

    print(dic_string_key[key])
