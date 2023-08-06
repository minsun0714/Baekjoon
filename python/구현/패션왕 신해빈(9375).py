from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

test_case_count = int(s.readline().strip())

for _ in range(test_case_count):
    dic = {}
    n = int(s.readline().strip())
    for _ in range(n):
        cloth, type = s.readline().strip().split()
        # dic[type] = 1 if not type in dic else dic[type] + 1
        dic[type] = dic.get(type, 0) + 1

    result = 1
    for type in dic:
        result *= (dic[type] + 1)
    print(result - 1)
