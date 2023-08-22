from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

stack = list(s.readline().strip())

layer = 0
count = 0

while stack:
    if stack[-2:] == [")", ")"]:
        layer += 1
        count += 1
    elif stack[-2:] == ["(", ")"]:
        count += layer
        stack.pop()
    else:
        layer -= 1
    stack.pop()

print(count)
