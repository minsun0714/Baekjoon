from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

n = int(s.readline().strip())

str_list = [int(i) for i in str(n)]

if not 0 in str_list or sum(str_list) % 3 > 0:
    print(-1)
else:
    str_list.sort(reverse=True)
    num = [str(i) for i in str_list]
    print(int("".join(num)))
