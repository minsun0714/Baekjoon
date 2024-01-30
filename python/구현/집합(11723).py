from sys import stdin as f

f = open("input.txt", "rt")  # 주석 처리해야 하는 부분

m = int(f.readline().strip())
s = set()

for _ in range(m):
    line = f.readline().strip()
    if line != 'all' and line != 'empty':
        line = line.split()
        action = line[0]
        num = int(line[1])
    else:
        action = line
        num = 0

    if action == 'add':
        s.add(num)

    elif action == 'remove':
        s.discard(num)

    elif action == 'check':
        if num in s:
            print(1)
        else:
            print(0)

    elif action == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)

    elif action == 'all':
        for i in range(1, 21):
            s.add(i)

    else:
        s.clear()
