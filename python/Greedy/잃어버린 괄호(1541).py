from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

formula = s.readline().strip()

formula = formula.split('-')

result = []
for f in formula:
    f = f.split('+')
    result.append(sum(list(map(int, f))))

answer = result[0]

for i in range(1, len(result)):
    answer -= result[i]

print(answer)
