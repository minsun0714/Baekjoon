from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분


def calculate(formula):
    replaced_formula = formula.replace(' ', '')
    res = eval(replaced_formula)
    if res == 0:
        print(formula)


def brute_force(depth, formula):
    if depth == t - 1:
        calculate(formula)
        return

    for i in range(3):
        brute_force(depth + 1, formula + operator_type[i] + str(depth + 2))


n = int(s.readline())
for _ in range(n):
    t = int(s.readline())
    operator_type = [' ', '+', '-']

    brute_force(0, '1')
    print()
